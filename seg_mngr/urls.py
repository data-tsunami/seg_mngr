from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from seg_mngr.views import ServerTaskUpdateView, CrossCheckCreateView
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'seg_mngr.views.home', name='home'),
    url(r'^server_manager/(?P<id_operating_system>.*)/$',
        'seg_mngr.views.server_manager',
        name='server_manager'),
    url(r'server_tasks/(?P<server_id>.*)/$', 'seg_mngr.views.server_tasks',
        name='server_tasks'),
    url(r'server_task_form/(?P<pk>\d+)/$',
        login_required(ServerTaskUpdateView.as_view()),
        name='server_task_form'),
    url(r'cross_check/create/(?P<server_id>.*)/$',
        login_required(CrossCheckCreateView.as_view()),
        name='server_task_form'),
    url(r'^report_tasks/$',
        'seg_mngr.views.report_tasks',
        name='report_taks'),
    url(r'^report_servers/$',
        'seg_mngr.views.report_servers',
        name='report_servers'),
    url(r'^cross_check/(?P<server_id>.*)/$',
        'seg_mngr.views.cross_check',
        name='cross_check'),
    url(r'^cross_check_tasks/(?P<server_id>.*)/$',
        'seg_mngr.views.cross_check_tasks',
        name='cross_check_tasks'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/', }, name='logout',),
)
