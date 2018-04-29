
from django.contrib import admin
from django.conf.urls import url, include
from server import views,api


urlpatterns = [
    url(r'^rundb/$', views.run_db),
    url(r'^collection/$', api.received_sys_info,name='data_recv'),
    url(r'^index/$', views.index,name='sys_data_index'),
    url(r'^system/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.host_info, name='host_info'),
    url(r'^get/cpu/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_cpu, name='get_cpu'),
    url(r'^get/mem/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_mem, name='get_mem'),
    # url(r'^get/pro/mem/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_pro_mem, name='get_pro_mem'),
    url(r'^get/disk/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_disk, name='get_disk'),
    url(r'^get/net/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_net, name='get_net'),
]
