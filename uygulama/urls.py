from django.conf.urls import url
from .views import *

app_name='uygulama'
urlpatterns = [
    url(r'^index$', uygulama_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', uygulama_detail, name='detail'),
    url(r'^create$', uygulama_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', uygulama_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', uygulama_delete, name='delete'),
]