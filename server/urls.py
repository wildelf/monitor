"""winMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from server import views,api


urlpatterns = [
    url(r'^rundb/$', views.run_db),
    url(r'^collection/$', api.received_sys_info,name='data_recv'),
    url(r'^index/$', views.get_sys_data,name='sys_data_index'),
    url(r'^system/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.host_info, name='host_info'),
    url(r'^get/cpu/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_cpu, name='get_cpu'),
    url(r'^get/mem/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.get_mem, name='get_mem'),
    url(r'^get/disk/(?P<machine_id>.+)/(?P<timing>\d+)/(?P<partition>\d+)/$', views.get_disk, name='get_disk'),
    url(r'^get/net/(?P<machine_id>.+)/(?P<timing>\d+)/(?P<net_id>\d+)/$', views.get_net, name='get_net'),
]
