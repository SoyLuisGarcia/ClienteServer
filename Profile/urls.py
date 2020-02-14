from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
#from Profile.views import CustonAuthToken

from Profile import views

urlpatterns = [
    #re_path(r'profile/$', CustonAuthToken.as_view()),
    re_path(r'example_lista3/$', views.ExampleList3.as_view()),
    re_path(r'example_EstadoCivil/$', views.EstadoCivil.as_view()),
    re_path(r'example_Ciudad/$', views.Ciudad.as_view()),
    re_path(r'example_Ocupacion/$', views.Ocupacion.as_view()),
    re_path(r'example_Estado/$', views.Estado.as_view()),
    re_path(r'example_Genero/$', views.Genero.as_view()),
]