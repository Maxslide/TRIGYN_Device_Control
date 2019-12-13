from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^AC/$',views.ac_page, name = 'AC'),
    url(r'^AC/(?P<ac_id>[0-9]+)/$', views.ac_change, name = 'AC_Change'),
    url(r'^AC/Change/(?P<acch_id>[0-9]+)/$', views.ac_makechange, name = 'AC_Change1'),
    url(r'^FAN/$',views.FAN_page, name = 'FAN'),
    url(r'^FAN/(?P<ac_id>[0-9]+)/$', views.fan_change, name = 'FAN_Change'),
    url(r'^FAN/Change/(?P<acch_id>[0-9]+)/$', views.fan_makechange, name = 'FAN_Change1'),
    url(r'^Geyser/$',views.Geyser_page, name = 'Geyser'),
    url(r'^Geyser/(?P<ac_id>[0-9]+)/$', views.Geyser_change, name = 'Geyser_Change'),
    url(r'^Geyser/Change/(?P<acch_id>[0-9]+)/$', views.Geyser_makechange, name = 'Geyser_Change1'),
    url(r'^Bulb/$',views.Bulb_page, name = 'Bulb'),
    url(r'^Bulb/(?P<ac_id>[0-9]+)/$', views.Bulb_change, name = 'Bulb_Change'),
    url(r'^Bulb/Change/(?P<acch_id>[0-9]+)/$', views.Bulb_makechange, name = 'Bulb_Change1'),
    url(r'^Wifi/$',views.Wifi_page, name = 'Wifi'),
    url(r'^Wifi/(?P<ac_id>[0-9]+)/$', views.Wifi_change, name = 'Wifi'),
    url(r'^Wifi/Change/(?P<acch_id>[0-9]+)/$', views.Wifi_makechange, name = 'Wifi_Change1'),
    url(r'^car_park/$', views.Car_Park_page, name = 'Car_park'),
    url(r'^car_park/book/$', views.Car_book, name = 'Car_book'),
    url(r'^car_park/remove/$', views.Car_remove, name = 'Car_book'),    
]