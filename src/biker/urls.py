from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from biker.views import *

urlpatterns = [
        url(r'^$', views.index),
        url(r'^accounts/login/$', login_index),
        url(r'^logout/$', logout),
        url(r'route/add/$', login_required(RutaCreate.as_view()), name='route-add'),
	url(r'search/event/$',views.search_event),
	url(r'search/group/$',views.search_group),
	url(r'search/route/$',views.search_route),
        url(r'route/delete/(?P<pk>[0-9]+)/$', login_required(RutaDelete.as_view()), name='route-delete'),
        url(r'route/detail/(?P<pk>[0-9]+)/$', RutaDetail.as_view(), name='route-detail'),
        url(r'route/update/(?P<pk>[0-9]+)/$', login_required(RutaUpdate.as_view()), name='route-update'),
        url(r'route/list/$', RutaListView.as_view(), name='ruta-list'),
        url(r'group/add/$', login_required(GrupoCreate.as_view()), name='group-add'),
        url(r'group/delete/(?P<pk>[0-9]+)/$', login_required(GrupoDelete.as_view()), name='group-delete'),
        url(r'group/detail/(?P<pk>[0-9]+)/$', GrupoDetail.as_view(), name='group-detail'),
        url(r'group/update/(?P<pk>[0-9]+)/$', login_required(GrupoUpdate.as_view()), name='group-update'),
        url(r'group/list/$', GrupoListView.as_view(), name='group-list'),
        url(r'event/add/$', login_required(EventoCreate.as_view()), name='event-add'),
        url(r'event/delete/(?P<pk>[0-9]+)/$', login_required(EventoDelete.as_view()), name='event-delete'),
        url(r'event/detail/(?P<pk>[0-9]+)/$', EventoDetail.as_view(), name='event-detail'),
        url(r'event/update/(?P<pk>[0-9]+)/$', login_required(EventoUpdate.as_view()), name='event-update'),
        url(r'event/list/$', EventoListView.as_view(), name='event-list'),
        url(r'solicitude/create/$', solicitud_create, name='solicitude-create'),
        url(r'solicitude/accept/$', login_required(solicitud_accept), name='solicitude-accept'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
