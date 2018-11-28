from django.urls import path
from dailyreport import views

app_name = 'daily'
urlpatterns = [
    path('', views.DailyReportView.as_view(), name='report'),
    path('myreport', views.MyReportView.as_view(), name='myreport'),
    path('create/', views.ReportCreateView.as_view(), name='report_create'),
    path('detail/', views.ReportDetailView.as_view(), name='report_detail')
]
