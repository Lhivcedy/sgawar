from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import FileField
from django.utils import timezone

# importar el modelo de tabla de usuario desde el administrador
from django.contrib.auth.models import User
# importar libreria de autentificacion
from django.contrib.auth import authenticate, logout, login as login_aut
# importar libreria decoradora que evita el ingreso a las paginas sin autorizacion
from django.contrib.auth.decorators import login_required, permission_required

import os


def create_path(instance, filename):
    return os.path.join(
        'archivos',
        'temas',
        str(instance.tema.id),
        filename
    )

# Create your models here.


class Gerencia(models.Model):
    id = IntegerField(primary_key=True)
    nombre_gerencia = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} {self.nombre_gerencia}'


class Tema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=1000)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.nombre}'


class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(
        auto_created=True, auto_now=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    file = FileField(upload_to=create_path)

    def __str__(self):
        return f'{self.id} {self.file}'

    def filename(self):
        return os.path.basename(self.file.name)


class Topico(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_topico = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.nombre_topico}'


class Capacitaciones(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True, auto_created=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
