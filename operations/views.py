from django.shortcuts import render, render_to_response
from .models import *
from django.views import View
from system.mixin import LoginRequiredMixin


class MyOpsView(LoginRequiredMixin, View):

    def get(self, request):
        title = "Ops"
        username = "Hi"
        ops_servers = OpsServer.objects.all()

        return render_to_response("operations/service_list.html", locals())


class OpsDetailView(LoginRequiredMixin, View):

    def get(self, request):
        title = "Ops"
        username = "Hi"
        ops_servers = OpsServer.objects.filter(id=id)

        return render_to_response("operations/service_more.html", locals())


class MyHostsView(LoginRequiredMixin, View):

    def get(self, request):
        title = "Ops"
        username = "Hi"
        ops_hosts = OpsHost.objects.filter(ops_server_id=id)

        return render_to_response("operations/hosts.html", locals())
