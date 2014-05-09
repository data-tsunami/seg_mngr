# -*- coding: utf-8 -*-

from django.db import models

class Task(models.Model):
    """
    Tareas de los servidores
    """
    name = models.CharField(max_length=64)
    description = models.TextField(verbose_name='Descripción')

    def __unicode__(self):
        return self.name  

class Server(models.Model):
    """
    Clase sevidor
    """
    name = models.CharField(max_length=64)    
    operating_system = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
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
    server = models.ForeignKey(Server)
    task = models.ForeignKey(Task)
    state = models.CharField(max_length = 64)

    def __unicode__(self):
        return u"Servidor {0} Tarea {1}".format(self.server.name, self.task.name)





