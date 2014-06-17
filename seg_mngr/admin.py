# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db.models import Count
from seg_mngr.models import ConfigIp, Server, Task, OperatingSystem, \
    Location, TaskGroup, ServerTask, PeriodicTask


# from django.db import models
class ConfigIpInLine(admin.StackedInline):
    model = ConfigIp
    extra = 1


class PeriodicTaskInLine(admin.TabularInline):
    model = PeriodicTask.server.through
    extra = 1
    verbose_name_plural = "Periodic Tasks"


class ServerAdmin(admin.ModelAdmin):
    inlines = [ConfigIpInLine, PeriodicTaskInLine]
    list_filter = ('operating_system__name', 'location__name',)


class ServerTaskAdmin(admin.ModelAdmin):
    list_display = ('server', 'task', 'state', 'comments',)


class ServerTaskComment(ServerTask):
    class Meta:
        proxy = True


class ServerTaskCommentAdmin(ServerTaskAdmin):
    readonly_fields = ('server', 'task', 'state',)
    fields = ('server', 'task', 'state', 'comments',)

    def queryset(self, request):
        return self.model.objects.all()


class PeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'frecuency', 'server_count')

    def queryset(self, request):
        return PeriodicTask.objects.annotate(server_count=Count('server'))

    def server_count(self, inst):
        return inst.server_count
    server_count.admin_order_field = 'server_count'


admin.site.register(ConfigIp)
admin.site.register(Server, ServerAdmin)
admin.site.register(Task)
admin.site.register(OperatingSystem)
admin.site.register(Location)
admin.site.register(TaskGroup)
admin.site.register(ServerTask)
admin.site.register(ServerTaskComment, ServerTaskCommentAdmin)
admin.site.register(PeriodicTask, PeriodicTaskAdmin)
