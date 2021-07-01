from core.views import agregartema, cerrar, index, login, temas
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('temas', temas, name='temas'),
    path('agregartema', agregartema, name='agregartema'),
    path('login', login, name='login'),
    path('cerrar', cerrar, name='cerrar')
]
