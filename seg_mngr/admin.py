# -*- coding: utf-8 -*-

from django.contrib import admin
from seg_mngr.models import ConfigIp, Server, Task, OperatingSystem


# from django.db import models
class ConfigIpInLine(admin.StackedInline):
    model = ConfigIp
    extra = 1


class ServerAdmin(admin.ModelAdmin):
    inlines = [ConfigIpInLine, ]


admin.site.register(ConfigIp)
admin.site.register(Server, ServerAdmin)
admin.site.register(Task)
admin.site.register(OperatingSystem)
