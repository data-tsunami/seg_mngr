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
    name = models.CharField(max_length=64, verbose_name='Operating system')

    def __unicode__(self):
        return self.name


class Location(models.Model):
    """
    Ubicación de un servidor
    """
    name = models.CharField(max_length=64, verbose_name='Location')
    
    def __unicode__(self):
        return self.name


class Server(models.Model):
    """
    Clase sevidor
    """
    PUBLICO = 1
    NAT = 2
    LAN = 3
    NIVEL_CHOICES = (
                     (PUBLICO,"Público"),
                     (NAT,"NAT"),
                     (LAN,"LAN"),
                     )
    name = models.CharField(max_length=64)
    operating_system = models.ForeignKey(OperatingSystem)    
    location = models.ForeignKey(Location)
    task = models.ManyToManyField(Task, through='ServerTask', blank=True)
    nivel_exposicion = models.IntegerField(max_length=2, choices=NIVEL_CHOICES, 
                                           default=LAN)

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
    PENDIENTE = 'P'
    NO_APLICA = 'NA'
    EN_CURSO = 'EC'
    FINALIZADA = 'F'
    STATE_CHOICES = (
        (PENDIENTE, 'Pendiente'),
        (NO_APLICA, 'No aplica'),
        (EN_CURSO, 'En curso'),
        (FINALIZADA, 'Finalizada'),
    )
    server = models.ForeignKey(Server)
    task = models.ForeignKey(Task)
    state = models.CharField(max_length=64, choices=STATE_CHOICES,
        default=PENDIENTE)

    def __unicode__(self):
        return u"Servidor {0} Tarea {1}".format(self.server.name,
            self.task.name)
