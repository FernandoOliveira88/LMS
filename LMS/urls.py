from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('', index),
    path('index', index),
    path('detalhecurso', detalhecurso),
    path('disciplinas', disciplinas),
    path('listascursos', listascursos),
    path('noticias', noticias),
    path('login', login),
    path('area_do_professor', area_do_professor),
    path('area_do_aluno', area_do_aluno),
    path('admin/', admin.site.urls),
]