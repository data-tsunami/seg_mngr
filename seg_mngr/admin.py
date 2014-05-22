# -*- coding: utf-8 -*-

from django.contrib import admin
from seg_mngr.models import ConfigIp, Server, Task, OperatingSystem, Location, TaskGroup, ServerTask


# from django.db import models
class ConfigIpInLine(admin.StackedInline):
    model = ConfigIp
    extra = 1


class ServerAdmin(admin.ModelAdmin):
    inlines = [ConfigIpInLine, ]
    list_filter = ('operating_system__name','location__name',)


class ServerTaskAdmin(admin.ModelAdmin):
    list_display = ('server','task','state','comments')

    
class ServerTaskComment(ServerTask):
    class Meta:
        proxy = True


class ServerTaskCommentAdmin(ServerTaskAdmin):
    readonly_fields =('server','task','state',)
    fields = ('server','task','state','comments')
    def queryset(self,request):        
        return self.model.objects.all()


admin.site.register(ConfigIp)
admin.site.register(Server, ServerAdmin)
admin.site.register(Task)
admin.site.register(OperatingSystem)
admin.site.register(Location)
admin.site.register(TaskGroup)
admin.site.register(ServerTask)
admin.site.register(ServerTaskComment, ServerTaskCommentAdmin)
