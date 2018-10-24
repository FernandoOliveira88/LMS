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
    path('admin/', admin.site.urls),
]