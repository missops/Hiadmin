from django.urls import path, include
from navigation import views

app_name = "navi"
urlpatterns = [
    path('index/', views.NaviIndexView.as_view(), name="navi"),
    path('add/', views.NaviAddView.as_view(), name="navi_add"),
]
