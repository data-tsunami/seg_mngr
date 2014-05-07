# -*- coding: utf-8 -*-

from seg_mngr.models import ConfigIp, Server, Task 
from django.contrib import admin
#from django.db import models

class ConfigIpInLine(admin.StackedInline):
    model = ConfigIp
    extra = 1

class ServerAdmin(admin.ModelAdmin):
    inlines =[ConfigIpInLine,]    


admin.site.register(ConfigIp)
admin.site.register(Server, ServerAdmin)
admin.site.register(Task)
