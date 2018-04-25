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
from server import views


urlpatterns = [
    url(r'^collection/$', views.received_sys_info,name='data_recv'),
    url(r'^index/$', views.get_sys_data,name='sys_data_index'),
    url(r'^system/(?P<machine_id>.+)/(?P<timing>\d+)/$', views.host_info, name='host_info'),
    url(r'^get/cpu/(?P<hostname>.+)/(?P<timing>\d+)/$', views.get_cpu, name='get_cpu'),

]
