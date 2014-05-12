from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seg_mngr.models import Server, Task, ServerTask

def home(request):
    return render_to_response("seg_mngr/index.html")

def server_manager(request):
    matriz = {}    
    for tareas in Task.objects.all():
            for servidor in Server.objects.all():
                try:
                    estado = ServerTask.objects.get(task=tareas, server= servidor)
                except ServerTask.DoesNotExist:
                    estado = None
                if estado is not None:
                    matriz[(tareas.id,servidor.id)] = estado.state
                else:
                    matriz[(tareas.id,servidor.id)] = 'Falta'
    for k,v in matriz.items():
        print  (k,v)
    contexto = {
        'servers': Server.objects.all(),
        'tasks': Task.objects.all(),
        'matriz': matriz,
    }
    return render_to_response(
        "seg_mngr/server_manager.html",contexto, 
        context_instance=RequestContext(request))
