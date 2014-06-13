from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seg_mngr.models import Server, Task, ServerTask, CrossCheck
from seg_mngr.forms import ServerTaskForm, ServerSearchForm, CrossCheckForm
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
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

    pie_chart = pygal.Pie()
    pie_chart.title = 'Estado de las tareas'
    for item in tabla_task_state:
        pie_chart.add(item['state'], item['cant_state'])

    pie_chart.render_to_file('bar_chart.svg')
    contexto = {
        'tabla_task': tabla_task_state,
        'chart': pie_chart,
    }
    return render_to_response(
        "seg_mngr/report_tasks.html", contexto,
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


class CrossCheckCreateView(CreateView):
    model = CrossCheck
    template_name = 'seg_mngr/cross_check_form.html'
    form_class = CrossCheckForm

    def form_valid(self, form):
        server = Server.objects.get(pk=self.kwargs['server_id'])
        user = self.request.user
        form.instance.server = server
        form.instance.autor = user
        return super(CrossCheckCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('server_tasks', kwargs={'server_id':
            self.kwargs['server_id']})

    def get_context_data(self, **kwargs):
        context = super(CrossCheckCreateView, self).get_context_data(**kwargs)
        server = Server.objects.get(pk=self.kwargs['server_id'])
        context['server'] = server
        return context
