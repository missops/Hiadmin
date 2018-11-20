from django.shortcuts import render
from navigation import models,forms

# Create your views here.

def index(request):
    title = 'Navi'
    username = request.session.get('username')
    allnavi = models.Navi.objects.all()
    return render(request, "navigation/index.html",locals())

def add(request):
    title = 'Navi Add'
    username = request.session.get('username')
    if request.method == "POST":
        n_form = forms.NaviForm(request.POST)
        print(n_form)
        if n_form.is_valid():
            n_form.save()
            tips = u"增加成功！"

        else:
            tips = u"增加失败！"

        return render(request, "navigation/add.html", locals())
    else:

        n_form = forms.NaviForm()
        return render(request, "navigation/add.html", locals())