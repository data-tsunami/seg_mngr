# -*- coding: utf-8 -*-

from django.db import models


class TaskGroup(models.Model):
    """
    Grupo de Tareas
    """
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name


class Task(models.Model):
    """
    Tareas de los servidores
    """
    name = models.CharField(max_length=64)
    description = models.TextField(verbose_name='Descripción')
    task_group = models.ForeignKey(TaskGroup)

    def __unicode__(self):
        return self.name


class OperatingSystem(models.Model):
    """
    Clase Sistema Operativo
    """
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    """
    Ubicación de un servidor
    """
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name


class Server(models.Model):
    """
    Clase sevidor
    """
    name = models.CharField(max_length=64)
    operating_system = models.ForeignKey(OperatingSystem)    
    location = models.ForeignKey(Location)
    task = models.ManyToManyField(Task, through='ServerTask', blank=True)

    def __unicode__(self):
        return self.name


class ConfigIp(models.Model):
    """
    Una configuracion Ip del servidor
    """
    ip_address = models.CharField(max_length=64)
    server = models.ForeignKey(Server)

    def __unicode__(self):
        return self.ip_address


class ServerTask(models.Model):
    """
    Estado de la tarea por servidor
    """
    Pendiente = 'P'
    No_Aplica = 'NA'
    En_Curso = 'EC'
    Finalizada = 'F'
    STATE_CHOICES = (
        (Pendiente, 'Pendiente'),
        (No_Aplica, 'No aplica'),
        (En_Curso, 'En curso'),
        (Finalizada, 'Finalizada'),
    )
    server = models.ForeignKey(Server)
    task = models.ForeignKey(Task)
    state = models.CharField(max_length=64, choices=STATE_CHOICES,
        default=Pendiente)

    def __unicode__(self):
        return u"Servidor {0} Tarea {1}".format(self.server.name,
            self.task.name)
