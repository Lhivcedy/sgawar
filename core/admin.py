from core.models import Archivos, ArchivosCapacitacion, Capacitaciones, Duracion, Frecuencia, Gerencia, Tema, Topico
from django.contrib import admin

# Register your models here.
admin.site.register(Tema)
admin.site.register(Archivos)
admin.site.register(Gerencia)
admin.site.register(Topico)
admin.site.register(Frecuencia)
admin.site.register(Duracion)
admin.site.register(Capacitaciones)
admin.site.register(ArchivosCapacitacion)