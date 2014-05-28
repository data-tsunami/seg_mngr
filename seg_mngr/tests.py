# -*- coding: utf-8 -*-
from django.test import TestCase
from seg_mngr.models import Server, Task, ServerTask, OperatingSystem, Location, TaskGroup
import generator_matriz
# Create your tests here.


class TestMatrixGenerator(TestCase):

    def test_matrix_is_generated(self):
        """Tests that a matrix is generated successfully"""

        # TODO: crear servidores server_1, server_2, server_3
        operating_system_1= OperatingSystem.objects.create(name='linux')
#         operating_system_1 = OperatingSystem.objects.get(pk=1)
        operating_system_2= OperatingSystem.objects.create(name='windows')
#         operating_system_2 = OperatingSystem.objects.get(pk=2)
#         location_1 = Location.objects.get(pk=1)
#         location_2 = Location.objects.get(pk=2)
        location_1 =Location.objects.create(name='Amazon')
        location_2 =Location.objects.create(name='España')
        server_1 = Server.objects.create(name='Dhcp', operating_system=operating_system_1,location=location_2, nivel_exposicion=1)
        server_2 = Server.objects.create(name='DNS', operating_system=operating_system_1,location=location_1, nivel_exposicion=2)
        server_3 = Server.objects.create(name='Maestro', operating_system=operating_system_2,location=location_2, nivel_exposicion=3)

        # TODO: crear tasks task_1, task_2, task_3
#         task_group_1 = TaskGroup.objects.get(pk=1)
#         task_group_2 = TaskGroup.objects.get(pk=2)
        task_group_1 = TaskGroup.objects.create(name='Gestión Usuarios')
        task_group_2 = TaskGroup.objects.create(name='Administración de red')
        task_1 = Task.objects.create(name='modificar user admin', description='modifcar user', task_group=task_group_1)
        task_2 = Task.objects.create(name='configurar ftp', description='configurar', task_group=task_group_2)
        task_3 = Task.objects.create(name='modificar permisos del grupo contable', description='modificar permisos a grupo', task_group=task_group_1)

        # TODO: cambiar estados:
        #  s1 t1 -> NO_APLICA
        #  s2 t3 -> EN_CURSO
        #  s1 t2 -> FINALIZADA
        try:
            server_task = ServerTask.objects.get(task=task_1, server=server_1)
        except ServerTask.DoesNotExist:
            server_task = None
        if server_task is not None: #actualiza state en servertask
            ServerTask.objects.filter(task=task_1, server=server_1).update(
                state='NA')
        else: # si no tiene un serverTask lo crea
            server_task = ServerTask(task=task_1, server=server_1,
                state='NA')
            server_task.save()
        try:
            server_task = ServerTask.objects.get(task=task_3, server=server_2)
        except ServerTask.DoesNotExist:
            server_task = None
        if server_task is not None: #actualiza state en servertask
            ServerTask.objects.filter(task=task_3, server=server_2).update(
                state='EC')
        else: # si no tiene un serverTask lo crea
            server_task = ServerTask(task=task_3, server=server_2,
                state='EC')
            server_task.save()
        try:
            server_task = ServerTask.objects.get(task=task_2, server=server_1)
        except ServerTask.DoesNotExist:
            server_task = None
        if server_task is not None: #actualiza state en servertask
            ServerTask.objects.filter(task=task_2, server=server_1).update(
                state='F')
        else: # si no tiene un serverTask lo crea
            server_task = ServerTask(task=task_2, server=server_1,
                state='F')
            server_task.save()
        # -----

        # TODO: generar matrix
        matriz = generator_matriz.generator_matriz()
        # self.assertXxxx() de que la matrix contiene los datos correctos
        self.assertIsNotNone(matriz, 'funciona bien')
