from django.urls import path
from dailyreport import views

app_name = 'daily'
urlpatterns = [
    path('', views.DailyReportView.as_view(), name='report'),
    path('report/create', views.ReportCreateView.as_view(), name='report_create')
]
