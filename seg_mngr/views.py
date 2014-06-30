from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seg_mngr.models import Server, Task, ServerTask, CrossCheck, \
    CrossCheckTask
from seg_mngr.forms import ServerTaskForm, ServerSearchForm, \
    CrossCheckTaskSelectionForm
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q
import generator_matriz
import datetime
import pygal


def home(request):
    return HttpResponseRedirect('/server_manager/' + str(0))


# Vista para el template seg_mnger/server_manager.html
# Te arma la matriz donde muestra los estado de la tarea por servidor
@login_required(login_url='/accounts/login/')
def server_manager(request, id_operating_system):
    matriz, servidores = generator_matriz.generator_matriz(
        int(id_operating_system))
    if request.method == 'POST':
        form = ServerSearchForm(request.POST, request.FILES)
        if form.is_valid():
            operating_system_selected = form.cleaned_data['operating_system']
            return HttpResponseRedirect('/server_manager/' +
                                        operating_system_selected)

    else:
        form = ServerSearchForm()

    contexto = {
        'servers': servidores,
        'matriz': matriz,
        'form': form,
        'operating_system_id': id_operating_system,
    }
    return render_to_response(
        "seg_mngr/server_matrix.html", contexto,
        context_instance=RequestContext(request))


# vista del servidor muestra los estados de las tareas de un servidor
# Actualiza el estado de la tarea
# template: seg_mngr/server_task.html
@login_required(login_url='/accounts/login/')
def server_tasks(request, server_id):
    servidor = Server.objects.get(pk=server_id)
    if request.method == 'POST':  # recuperar los datos de los submmit
        update_task = [k for k in request.POST.keys()
            if k.startswith(server_id + '-')]
        task_id = update_task[0].split('-')[1]
        update_state = update_task[0].split('-')[2]
        tarea = Task.objects.get(pk=task_id)
        try:
            server_task = ServerTask.objects.get(task=tarea, server=servidor)
            ServerTask.objects.filter(task=tarea, server=servidor).update(
                state=update_state, date_update_state=datetime.datetime.now(),
                autor_update_state=request.user)
        except ServerTask.DoesNotExist:
            server_task = ServerTask(task=tarea, server=servidor,
                state=update_state, date_update_state=datetime.datetime.now(),
                autor_update_state=request.user)
            server_task.save()
        return HttpResponseRedirect('/server_tasks/' + server_id)

    contexto = {
        'servidor': Server.objects.get(pk=server_id),
        'matriz': generator_matriz.genertator_matriz_server(servidor),
    }
    return render_to_response(
        "seg_mngr/server_tasks.html", contexto,
        context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def report_tasks(request):
    tabla_task_state = ServerTask.objects.values("state").annotate(
        cant_state=Count("state"))
    tabla_dic_state = {ServerTask.PENDIENTE: 0, ServerTask.EN_CURSO: 0,
                       ServerTask.NO_APLICA: 0, ServerTask.FINALIZADA: 0}
    pie_chart = pygal.Pie()
    pie_chart.title = 'Estado de las tareas'
    servers = Server.objects.all()
    tasks = Task.objects.all()
    total_taks = servers.count() * tasks.count()
    server_tasks = ServerTask.objects.all()
    total_pendiente = total_taks - server_tasks.count()
    for item in tabla_task_state:
        if item['state'] == ServerTask.PENDIENTE:
            item['cant_state'] += total_pendiente
            tabla_dic_state[ServerTask.PENDIENTE] = item['cant_state']
            pie_chart.add('Pendiente', item['cant_state'])
        elif item['state'] == ServerTask.NO_APLICA:
            tabla_dic_state[ServerTask.NO_APLICA] = item['cant_state']
            pie_chart.add('No aplica', item['cant_state'])
        elif item['state'] == ServerTask.EN_CURSO:
            tabla_dic_state[ServerTask.EN_CURSO] = item['cant_state']
            pie_chart.add('En curso', item['cant_state'])
        elif item['state'] == ServerTask.FINALIZADA:
            tabla_dic_state[ServerTask.FINALIZADA] = item['cant_state']
            pie_chart.add('Finalizada', item['cant_state'])
    pie_chart.render_to_file('bar_chart.svg')
    contexto = {
        'tabla_task': tabla_dic_state,
        'chart': pie_chart,
        'total_tasks': total_taks,
    }
    return render_to_response(
        "seg_mngr/report_tasks.html", contexto,
        context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def report_servers(request):
    server_finalizados = 0
    tasks = Task.objects.all().count()
    for server in Server.objects.all():
        server_tasks = ServerTask.objects.filter(Q(server=server),
            Q(state=ServerTask.FINALIZADA) | Q(state=ServerTask.NO_APLICA))
        if tasks == server_tasks.count():
            server_finalizados += 1
    total_servers = Server.objects.all().count()
    server_no_finalizados = total_servers - server_finalizados
    pie_chart = pygal.Pie()
    pie_chart.title = 'Estado de los servidores'
    pie_chart.add('Finalizados', server_finalizados)
    pie_chart.add('No finalizados', server_no_finalizados)
    pie_chart.render_to_file('bar_chart_server.svg')
    contexto = {
        'server_finalizados': server_finalizados,
        'server_no_finalizados': server_no_finalizados,
        'chart': pie_chart,
        'total_servers': total_servers,
    }
    return render_to_response(
        "seg_mngr/report_servers.html", contexto,
        context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def cross_check(request, server_id):
    if request.method == 'POST':
        print request.POST.keys()
        tasks_check_id = [k for k in request.POST.keys()
            if k.startswith('task-')]

        tasks_checks = []
        for task_id in tasks_check_id:
            tasks_checks.append(task_id.split('-')[1])

        request.session['tasks'] = tasks_checks
        return HttpResponseRedirect('/cross_check_tasks/' + server_id)

    tasks_dic = ServerTask.objects.values('task').filter(
        Q(server=server_id), Q(state=ServerTask.FINALIZADA) |
        Q(state=ServerTask.NO_APLICA))
    tasks = []
    for tarea in tasks_dic:
        task = Task.objects.get(pk=tarea['task'])
        tasks.append(task)
    contexto = {
        'server': Server.objects.get(pk=server_id),
        'tasks': tasks
    }
    return render_to_response(
        "seg_mngr/cross_check.html", contexto,
        context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def cross_check_tasks(request, server_id):
    cross_check = CrossCheck()
    user = request.user
    server = Server.objects.get(pk=server_id)
    cross_check.autor = user
    cross_check.server = server

    if request.method == 'POST':
        success_tasks = []
        cross_check.save()
        update_task = [k for k in request.POST.keys()
            if k.startswith('task-')]
        for task_id in update_task:
            cross_check_task = CrossCheckTask()
            cross_check_task.cross_check = cross_check
            task = Task.objects.get(pk=task_id.split('-')[1])
            cross_check_task.task = task
            success_tasks.append(int(task_id.split('-')[2]))
            cross_check_task.success = int(task_id.split('-')[2])
            cross_check_task.save()
        sum_success = 0
        for sum_task in success_tasks:
            sum_success += sum_task
        if sum_success == len(success_tasks):
            cross_check.success = True
            cross_check.save()
        return HttpResponseRedirect('/server_tasks/' + server_id)

    tasks_id = request.session['tasks']
    tasks = []
    for t_id in tasks_id:
        task = Task.objects.get(pk=t_id)
        tasks.append(task)
    contexto = {
        'server': Server.objects.get(pk=server_id),
        'tasks': tasks,
        'tasks_len': len(tasks)
    }
    return render_to_response(
        "seg_mngr/cross_check_tasks.html", contexto,
        context_instance=RequestContext(request))


def cross_check_result(request, cross_check_task_id):
    servidor = CrossCheck.objects.values('server').get(pk=cross_check_task_id)
    server = Server.objects.get(pk=servidor['server'])
    contexto = {
        'result': CrossCheckTask.objects.filter(
            cross_check=cross_check_task_id),
        'server': server
    }
    return render_to_response(
        "seg_mngr/cross_check_result.html", contexto,
        context_instance=RequestContext(request))


class ServerTaskUpdateView(UpdateView):
    model = ServerTask
    template_name = 'seg_mngr/server_task_form.html'
    form_class = ServerTaskForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ServerTaskUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('server_tasks', args=[self.object.server.pk])
