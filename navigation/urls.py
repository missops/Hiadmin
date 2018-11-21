from django.urls import path, include
from navigation import views

app_name = "navi"
urlpatterns = [
    path('index/', views.index, name="navi"),
    path('add/', views.add, name="navi_add"),

]
