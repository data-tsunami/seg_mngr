# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import markdown
from django.db import models
from django.contrib.auth.models import User


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
        (PUBLICO, "Público"),
        (NAT, "NAT"),
        (LAN, "LAN"),
    )
    name = models.CharField(max_length=64)
    operating_system = models.ForeignKey(OperatingSystem)
    location = models.ForeignKey(Location)
    task = models.ManyToManyField(Task, through='ServerTask', blank=True)
    nivel_exposicion = models.IntegerField(max_length=2, choices=NIVEL_CHOICES,
                                           default=LAN)

    def __unicode__(self):
        return self.name

    def getIp(self):
        return ConfigIp.objects.filter(server=self)
    
    def get_cross_check(self):
        return CrossCheck.objects.filter(server=self).order_by('check_date')


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
    comments = models.TextField(default='', blank=True)
    date_update_state = models.DateTimeField()
    autor_update_state = models.ForeignKey(User)

    def get_comentario_as_forhtml(self):
        if self.comments != '':
            return markdown.markdown(self.comments)
        else:
            return self.comments

    def tiene_comentario(self):
        return len(self.comments.strip()) > 0

    def __unicode__(self):
        return u"Servidor {0} Tarea {1}".format(self.server.name,
            self.task.name)


class CrossCheck(models.Model):
    """
    Control cruzado sobre servidor
    """
    server = models.ForeignKey(Server)
    autor = models.ForeignKey(User)
    check_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    success = models.BooleanField(default=False, verbose_name="Es exitoso")

    def __unicode__(self):
        return u"Control cruzado sobre servidor {0} realizado por {1}".format(
            self.server, self.autor.username)


class PeriodicTask(models.Model):
    """
    Clase de tareas periodica
    """
    FRECUENCY_CHOICES = (
        (1, 'tareas mensuales'),
        (2, 'tareas a realizar cada 2 meses'),
        (3, 'tareas a realizar cada 3 meses'),
        (4, 'tareas a realizar cada 4 meses'),
        (6, 'tareas a realizar cada 6 meses'),
        (9, 'tareas a realizar cada 9 meses'),
        (12, 'tareas a realizar cada 12 meses'),
    )
    name = models.CharField(max_length=64)
    description = models.TextField(verbose_name='Descripción')
    frecuency = models.PositiveIntegerField(choices=FRECUENCY_CHOICES)
    server = models.ManyToManyField(Server)

    def __unicode__(self):
        return u"Tarea periódica: " + self.name
