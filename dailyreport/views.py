from django.shortcuts import render
from dailyreport import models
from django.views.generic.base import View

# Create your views here.
class MyReportView(View):

    def get(self, request):
        return render(request, 'dailyreport/report.html')


