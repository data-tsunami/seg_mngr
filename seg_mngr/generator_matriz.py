'''
Created on 28/05/2014

@author: federico
'''
import markdown
from seg_mngr.models import ServerTask, Task, Server, CrossCheck


# def generator_matriz():
#     matriz = {}
#     for tareas in Task.objects.all().order_by('task_group'):
#         for servidor in Server.objects.all():
#             try:
#                 server_task = ServerTask.objects.get(task=tareas,
#                     server=servidor)
#             except ServerTask.DoesNotExist:
#                 server_task = None
#             if server_task is not None:
#                 comentario = markdown.markdown(server_task.comments)
#                 matriz[(tareas.id, servidor.id)] = (server_task.state,
#                                                     comentario)
#             else:
#                 matriz[(tareas.id, servidor.id)] = ServerTask.PENDIENTE
#     return matriz


def generator_matriz(id_operating_system):
    matriz = []
    servidores = Server.objects.all()
    if(id_operating_system != 0):
        servidores = Server.objects.filter(
            operating_system=id_operating_system)

    server_task_vacio = ServerTask()

    for tarea in Task.objects.all().order_by('task_group'):
        fila = []
        # una fila contiene: en primer lugar una task y en segundo
        # lugar una lista con los datos de los servidores para c/u columna
        fila.append(tarea)
        datos_servidores = []
        fila.append(datos_servidores)
        for servidor in servidores:
            try:
                server_task = ServerTask.objects.get(task=tarea,
                    server=servidor)
                datos_servidores.append(server_task)
            except ServerTask.DoesNotExist:
                datos_servidores.append(server_task_vacio)

        matriz.append(fila)
    return matriz, servidores


# def genertator_matriz_server(servidor):
#     matriz = {}
#     for tareas in Task.objects.all():
#         try:
#             server_task = ServerTask.objects.get(task=tareas,
#                        server=servidor)
#         except ServerTask.DoesNotExist:
#             server_task = None
#         if server_task is not None:
#             comentario = markdown.markdown(server_task.comments)
#             matriz[tareas] = (server_task.state, comentario, server_task.id)
#         else:
#             comentario = markdown.markdown('No hay comentarios')
#             matriz[tareas] = (ServerTask.PENDIENTE, comentario, 0)
#
#     return matriz


def genertator_matriz_server(servidor):
    matriz = []
    server_task_vacio = ServerTask()

    for tarea in Task.objects.all().order_by('task_group'):
        fila = []
        # una fila contiene: en primer lugar una task y en segundo
        # lugar los datos de la tarea con respecto a este servidor
        fila.append(tarea)
        try:
            server_task = ServerTask.objects.get(task=tarea, server=servidor)
            fila.append(server_task)
        except ServerTask.DoesNotExist:
            fila.append(server_task_vacio)
        cross_check = CrossCheck.objects.get_cross_check_last(servidor, tarea)
        print cross_check
        if cross_check:
            fila.append(cross_check)
        else:
            fila.append("no hay controles cruzado")

        matriz.append(fila)
    return matriz