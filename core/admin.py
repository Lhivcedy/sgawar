from core.models import Archivos, Capacitaciones, Gerencia, Tema, Topico
from django.contrib import admin

# Register your models here.
admin.site.register(Tema)
admin.site.register(Archivos)
admin.site.register(Gerencia)
admin.site.register(Topico)
admin.site.register(Capacitaciones)