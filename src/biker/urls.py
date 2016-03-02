from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from biker.views import *

urlpatterns = [
        url(r'^$', views.index),
        url(r'^login/$', login),
        url(r'^logout/$', logout),
        url(r'route/add/$', RutaCreate.as_view(), name='route-add'),
        url(r'route/delete/(?P<pk>[0-9]+)/$', RutaDelete.as_view(), name='route-delete'),
        url(r'route/detail/(?P<pk>[0-9]+)/$', RutaDetail.as_view(), name='route-detail'),
        url(r'route/update/(?P<pk>[0-9]+)/$', RutaUpdate.as_view(), name='route-update'),
        url(r'route/list/$', RutaListView.as_view(), name='ruta-list'),
        url(r'group/add/$', GrupoCreate.as_view(), name='group-add'),
        url(r'group/delete/(?P<pk>[0-9]+)/$', GrupoDelete.as_view(), name='group-delete'),
        url(r'group/detail/(?P<pk>[0-9]+)/$', GrupoDetail.as_view(), name='group-detail'),
        url(r'group/update/(?P<pk>[0-9]+)/$', GrupoUpdate.as_view(), name='group-update'),
        url(r'group/list/$', GrupoListView.as_view(), name='group-list'),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.event_detail),
	url(r'^delete/evento/(?P<pk>[0-9]+)/$', views.delete_evento),
        url(r'^eventos/$', views.events_list),
        url(r'^registrar/evento/$', views.registrar_evento, name='registrar_evento'),
        url(r'^evento/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
