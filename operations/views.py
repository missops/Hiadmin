from django.shortcuts import render, render_to_response
from .models import *


# Create your views here.

def ops_server(request):
    title = "Ops"
    username = "Hi"
    ops_servers = OpsServer.objects.all()

    return render_to_response("operations/service_list.html", locals())

def ops_server_more(request,id):
    title = "Ops"
    username = "Hi"
    ops_servers = OpsServer.objects.filter(id=id)

    return render_to_response("operations/service_more.html", locals())


def ops_hosts(request,id):
    id = int(id)
    title = "Ops"
    username = "Hi"
    ops_hosts = OpsHost.objects.filter(ops_server_id=id)

    return render_to_response("operations/hosts.html", locals())
