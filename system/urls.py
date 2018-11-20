from django.urls import path, include
from django.urls import re_path
from system import views_user,views_structure
from django.views.static import serve
from Hiadmin.settings import MEDIA_ROOT

app_name = 'sys'
urlpatterns = [
    path('index/',views_user.IndexView.as_view(),name='index'),
    path('login/', views_user.LoginView.as_view(), name='login'),
    path('logout/', views_user.LogoutView.as_view(), name='logout'),
    re_path(r'media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
     # path('basic/structure/', views_structure.StructureView.as_view(), name='basic-structure'),
     # path('basic/structure/create/', views_structure.StructureCreateView.as_view(), name='basic-structure-create'),
    # path('basic/structure/list/', views_structure.StructureListView.as_view(), name='basic-structure-list'),
    # path('basic/structure/delete/', views_structure.StructureDeleteView.as_view(), name='basic-structure-delete'),
    # path('basic/structure/add_user/', views_structure.Structure2UserView.as_view(), name='basic-structure-add_user'),
]