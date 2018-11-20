from django.urls import path,re_path
from operations import views

app_name = 'ops'
urlpatterns = [
    path('service/', views.ops_server, name='service'),
    re_path('service/(\d+)/',views.ops_server_more, name='service_more'),

    re_path('hosts/(\d+)/',views.ops_hosts, name='hosts_id')
]
