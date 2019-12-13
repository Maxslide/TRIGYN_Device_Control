from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^devices/AC/$', views.AC_all, name='AC_all'),
    url(r'^devices/AC/(?P<ac_id>[0-9]+)/$', views.AC_part, name='AC_part'),
    url(r'^devices/FAN/$', views.Fan_all, name='FAN_all'),
    url(r'^devices/FAN/(?P<ac_id>[0-9]+)/$', views.Fan_part, name='FAN_part'),
    url(r'^devices/Geyser/$', views.Geyser_all, name='Geyser_all'),
    url(r'^devices/Geyser/(?P<ac_id>[0-9]+)/$', views.Geyser_part, name='Geyser_part'),
    url(r'^devices/Bulb/$', views.Bulb_all, name='Bulb_all'),
    url(r'^devices/Bulb/(?P<ac_id>[0-9]+)/$', views.Bulb_part, name='Bulb_part'),
    url(r'^devices/Wifi/$', views.Wifi_all, name='Wifi_all'),
    url(r'^devices/Wifi/(?P<ac_id>[0-9]+)/$', views.Wifi_part, name='Wifi_part'),
    
    
]
