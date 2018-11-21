from django.shortcuts import render
from django.views.generic.base import TemplateView

from .mixin import LoginRequiredMixin


class SystemView(LoginRequiredMixin, TemplateView):

    template_name = 'system/system_index.html'
