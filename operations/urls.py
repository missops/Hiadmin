from django.urls import path, re_path
from operations import views

app_name = 'ops'
urlpatterns = [
    path('service/', views.MyOpsView.as_view(), name='service'),
    re_path('service/(\d+)/', views.OpsDetailView.as_view(), name='service_more'),
    re_path('hosts/(\d+)/', views.MyHostsView.as_view(), name='hosts_id')
]
