'''
Created on 28/05/2014

@author: federico
'''
import markdown
from seg_mngr.models import ServerTask, Task, Server


def generator_matriz():
    matriz = {}
    for tareas in Task.objects.all():
        for servidor in Server.objects.all():
            try:
                server_task = ServerTask.objects.get(task=tareas,
                    server=servidor)
            except ServerTask.DoesNotExist:
                server_task = None
            if server_task is not None:
                matriz[(tareas.id, servidor.id)] = server_task.state
            else:
                matriz[(tareas.id, servidor.id)] = 'P'

    return matriz


def genertator_matriz_server(servidor):
    matriz = {}
    for tareas in Task.objects.all():
        try:
            server_task = ServerTask.objects.get(task=tareas, server=servidor)
        except ServerTask.DoesNotExist:
            server_task = None
        if server_task is not None:
            comentario = markdown.markdown(server_task.comments)
            matriz[tareas] = (server_task.state, comentario, server_task.id)
        else:
            comentario = markdown.markdown('No hay comentarios')
            matriz[tareas] = ('P', comentario, 0)

    return matriz