from os import name
from core.views import actualizartema, agregarcapacitacion, agregartema, buscar, capacitaciones, cargar_anexos, cargar_asistencia, cargar_invitados, cerrar, cerrar_hito, eliminar_adjunto, eliminar_adjunto_capacitacion, eliminar_adjunto_hito, eliminar_asistente, eliminar_capa, eliminar_hito, eliminar_invitado_capacitacion, eliminar_tema, index, login, temas, ver_hito, ver_invitados_hitos, vercapacitacion, vertema
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
    path('invitadoshitos/hito/<int:id>', ver_hito, name='verhito'),
    path('cargarinvitados', cargar_invitados, name="cargarinvitados"),
    path('cargarasistencia', cargar_asistencia, name="cargarasistencia"),
    path('cargaranexos', cargar_anexos, name="cargaranexos"),
    path('invitadoshitos/<int:id>', ver_invitados_hitos,
         name='detalle_capacitacion'),
    path('invitadoshitos/hito/eliminar_adjunto_hito',
         eliminar_adjunto_hito, name='eliminaradjuntohito'),
    path('invitadoshitos/hito/eliminar_hito',
         eliminar_hito, name='eliminarhito'),
    path('invitadoshitos/hito/cerrar_hito',
         cerrar_hito, name='cerrarhito'),
    path('invitadoshitos/hito/eliminar_asistente',
         eliminar_asistente, name='eliminarasistente')
]
