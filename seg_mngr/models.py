# -*- coding: utf-8 -*-

from django.db import models

class ConfigIp(models.Model):
	"""
	Una configuracion Ip del servidor
	"""
	ip_address = models.CharField(max_length=64)

 	def __unicode__(self):
 		return self.ip_address

class Server(models.Model):
	"""
	Clase sevidor
	"""
	name = models.CharField(max_length=64)
	address_ip = models.ForeignKey('ConfigIp')
	operating_system = models.CharField(max_length=64)
	location = models.CharField(max_length=64)

	def __unicode__(self):
 		return self.name

