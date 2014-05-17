from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seg_mngr.models import Server, Task, ServerTask


def home(request):
    return render_to_response("seg_mngr/index.html")


# Vista para el template seg_mnger/server_manager.html
# Te arma la matriz donde muestra los estado de la tarea por servidor
def server_manager(request):
    matriz = {}
    for tareas in Task.objects.all():
        for servidor in Server.objects.all():
            try:
                estado = ServerTask.objects.get(task=tareas,
                    server=servidor)
            except ServerTask.DoesNotExist:
                estado = None
            if estado is not None:
                if estado.state == ServerTask.Pendiente:
                    matriz[(tareas.id, servidor.id)] = 'Pendiente'
                if estado.state == ServerTask.No_Aplica:
                    matriz[(tareas.id, servidor.id)] = 'No aplica'
                if estado.state == ServerTask.En_Curso:
                    matriz[(tareas.id, servidor.id)] = 'En curso'
                if estado.state == ServerTask.Finalizada:
                    matriz[(tareas.id, servidor.id)] = 'Finalizada'
            else:
                matriz[(tareas.id, servidor.id)] = 'Pendiente'
    contexto = {
        'servers': Server.objects.all(),
        'tasks': Task.objects.all(),
        'matriz': matriz,
    }
    return render_to_response(
        "seg_mngr/server_manager.html", contexto,
        context_instance=RequestContext(request))


# vista del servidor muestra los estados de las tareas de un servidor
# template: seg_mngr/server_task.html
def server_tasks(request, id_servidor):
    servidor = Server.objects.get(pk=id_servidor)
    if request.method == 'POST':
        update_task = [k for k in request.POST.keys()
            if k.startswith(id_servidor + '-')]
        task_id = update_task[0].split('-')[1]
        update_state = update_task[0].split('-')[2]
        tarea = Task.objects.get(pk=task_id)
        try:
            server_task = ServerTask.objects.get(task=tarea, server=servidor)
        except ServerTask.DoesNotExist:
            server_task = None
        if server_task is not None:
            ServerTask.objects.filter(task=tarea, server=servidor).update(
                state=update_state)
        else:
            server_task = ServerTask(task=tarea, server=servidor,
                state=update_state)
            server_task.save()
    matriz = {}
    for tareas in Task.objects.all():
        try:
            estado = ServerTask.objects.get(task=tareas, server=servidor)
        except ServerTask.DoesNotExist:
            estado = None
        if estado is not None:
            if estado.state == ServerTask.Pendiente:
                matriz[tareas] = 'Pendiente'
            if estado.state == ServerTask.No_Aplica:
                matriz[tareas] = 'No aplica'
            if estado.state == ServerTask.En_Curso:
                matriz[tareas] = 'En curso'
            if estado.state == ServerTask.Finalizada:
                matriz[tareas] = 'Finalizada'
        else:
            matriz[tareas] = 'Pendiente'
    contexto = {
        'servidor': Server.objects.get(pk=id_servidor),
        'tareas': matriz,
    }
    return render_to_response(
        "seg_mngr/server_tasks.html", contexto,
        context_instance=RequestContext(request))
