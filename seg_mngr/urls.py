from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'seg_mngr.views.home', name='home'),
    url(r'^server_manager/', 'seg_mngr.views.server_manager', name='server_manager_view'),
    url(r'^admin/', include(admin.site.urls)),
)
