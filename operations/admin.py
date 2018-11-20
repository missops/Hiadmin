from django.contrib import admin
from .models import OpsServer,OpsHost

# Register your models here.
admin.site.register(OpsServer)
admin.site.register(OpsHost)