from django.shortcuts import render
from navigation import models, forms
from django.views import View
from system.mixin import LoginRequiredMixin


class NaviIndexView(LoginRequiredMixin, View):

    def get(self, request):
        title = 'Navi'
        username = request.session.get('username')
        allnavi = models.Navi.objects.all()
        return render(request, "navigation/index.html", locals())


class NaviAddView(LoginRequiredMixin, View):

    def get(self, request):
        title = 'Navi Add'
        username = request.session.get('username')
        n_form = forms.NaviForm()
        return render(request, "navigation/add.html", locals())

    def post(self, request):
        n_form = forms.NaviForm(request.POST)
        print(n_form)
        if n_form.is_valid():
            n_form.save()
            tips = u"增加成功！"

        else:
            tips = u"增加失败！"

        return render(request, "navigation/add.html", locals())
