from django.urls import path, include
from django.urls import re_path
from system import views_user, views_structure, views
from django.views.static import serve
from Hiadmin.settings import MEDIA_ROOT

app_name = 'sys'
urlpatterns = [
    path('', views.SystemView.as_view(), name='system'),

    path('login/', views_user.LoginView.as_view(), name='login'),
    path('logout/', views_user.LogoutView.as_view(), name='logout'),
    re_path(r'media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    path('structure/', views_structure.StructureView.as_view(), name='structure'),
    path('structure/create/', views_structure.StructureCreateView.as_view(), name='structure_create'),
    path('structure/list/', views_structure.StructureListView.as_view(), name='structure_list'),
    path('structure/add_user/', views_structure.Structure2UserView.as_view(), name='structure_add_user'),

    path('user/', views_user.UserView.as_view(), name='user'),
    path('user/list/', views_user.UserListView.as_view(), name='user_list'),

]
