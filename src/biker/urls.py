from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.events_list),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.event_detail),
        url(r'^grupos/$', views.groups_list),
        url(r'^rutas/$', views.routes_list),
        url(r'^registrar/evento/$', views.registrar_evento, name='registrar_evento'),
        url(r'^registrar/grupo/$', views.registrar_grupo, name='registrar_grupo'),
        url(r'^registrar/ruta/$', views.registrar_ruta, name='registrar_ruta'),
    ]
