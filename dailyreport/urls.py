from django.urls import path
from dailyreport import views

urlpatterns= [
    path('',views.MyReportView.as_view(), name='daily')
]