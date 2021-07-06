from os import name
from core.views import actualizartema, agregarcapacitacion, agregartema, buscar, cerrar, eliminar_adjunto, eliminar_tema, index, login, temas, vertema
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('temas', temas, name='temas'),
    path('agregartema', agregartema, name='agregartema'),
    path('login', login, name='login'),
    path('cerrar', cerrar, name='cerrar'),
    path('tema/<int:id>', vertema, name='tema'),
    path('actualizartema', actualizartema, name='actualizartema'),
    path('tema/eliminar_tema', eliminar_tema, name='eliminartema'),
    path('tema/eliminar_adjunto', eliminar_adjunto, name='eliminaradjunto'),
    path('buscar', buscar, name='buscar'),
    path('agregarcapacitacion', agregarcapacitacion, name='agregarcapacitacion' )
]
