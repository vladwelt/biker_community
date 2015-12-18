from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.group_list),
        url(r'^evento/(?P<pk>[0-9]+)/$', views.event_detail),
    ]
