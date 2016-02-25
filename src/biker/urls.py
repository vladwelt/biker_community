from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.events_list),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.event_detail),
	url(r'^grupos/(?P<pk>[0-9]+)/$', views.group_detail),
	url(r'^rutas/(?P<pk>[0-9]+)/$', views.route_detail),
	url(r'^delete/group/(?P<pk>[0-9]+)/$', views.delete_group),
	url(r'^delete/ruta/(?P<pk>[0-9]+)/$', views.delete_ruta),
	url(r'^delete/evento/(?P<pk>[0-9]+)/$', views.delete_evento),
        url(r'^grupos/$', views.groups_list),
        url(r'^rutas/$', views.routes_list),
        url(r'^registrar/evento/$', views.registrar_evento, name='registrar_evento'),
        url(r'^registrar/grupo/$', views.registrar_grupo, name='registrar_grupo'),
        url(r'^registrar/ruta/$', views.registrar_ruta, name='registrar_ruta'),
        url(r'^evento/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
        url(r'^grupo/(?P<pk>[0-9]+)/edit/$', views.group_edit, name='group_edit'),
        url(r'^ruta/(?P<pk>[0-9]+)/edit/$', views.route_edit, name='route_edit'),
    ]
