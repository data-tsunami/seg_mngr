from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from seg_mngr.views import ServerTaskUpdateView
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'seg_mngr.views.home', name='home'),
    url(r'^server_manager/(?P<id_operating_systems>.*)/$',
        'seg_mngr.views.server_manager',
        name='server_manager'),
    url(r'server_tasks/(?P<id_servidor>.*)/$', 'seg_mngr.views.server_tasks',
        name='server_tasks'),
    url(r'server_task_form/(?P<pk>\d+)/$',
        login_required(ServerTaskUpdateView.as_view()),
        name='server_task_form'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
