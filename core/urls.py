from os import name
from core.views import actualizartema, agregarcapacitacion, agregartema, buscar, capacitaciones, cargar_invitados, cerrar, eliminar_adjunto, eliminar_adjunto_capacitacion, eliminar_capa, eliminar_invitado_capacitacion, eliminar_tema, index, login, temas, ver_invitados_hitos, vercapacitacion, vertema
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
    path('eliminar_capa', eliminar_capa, name='eliminarcapa'),
    path('capacitacion/eliminar_capa',
         eliminar_capa, name='eliminarcapacitacion'),
    path('tema/eliminar_adjunto', eliminar_adjunto, name='eliminaradjunto'),
    path('capacitacion/eliminar_adjunto_capa',
         eliminar_adjunto_capacitacion, name='eliminaraadjunto'),
    path('invitadoshitos/eliminar_invitado',
         eliminar_invitado_capacitacion, name='eliminarinvitado'),
    path('buscar', buscar, name='buscar'),
    path('agregarcapacitacion', agregarcapacitacion, name='agregarcapacitacion'),
    path('capacitaciones', capacitaciones, name='capacitaciones'),
    path('capacitacion/<int:id>', vercapacitacion, name='capacitacion'),
    path('cargarinvitados', cargar_invitados, name="cargarinvitados"),
    path('invitadoshitos/<int:id>', ver_invitados_hitos,
         name='detalle_capacitacion')
]
