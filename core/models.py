from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField, DateTimeField, IntegerField, TextField
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# importar el modelo de tabla de usuario desde el administrador
from django.contrib.auth.models import User
# importar libreria de autentificacion
from django.contrib.auth import authenticate, logout, login as login_aut
# importar libreria decoradora que evita el ingreso a las paginas sin autorizacion
from django.contrib.auth.decorators import login_required, permission_required

import os
import datetime


def create_path(instance, filename):
    return os.path.join(
        'archivos',
        'temas',
        str(instance.tema.id),
        filename
    )


def create_path_capacitaciones(instance, filename):
    return os.path.join(
        'archivos',
        'capacitaciones',
        str(instance.capacitacion.id),
        filename
    )


def create_path_hito(instance, filename):
    return os.path.join(
        'archivos',
        'hitos',
        str(instance.hito.id),
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


class Frecuencia(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_frecuencia = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.nombre_frecuencia}'


class Duracion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_duracion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.nombre_duracion}'


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capacitador = models.BooleanField(default=False)
    coordinador = models.BooleanField(default=False)
    alumno = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'


class Capacitaciones(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True, auto_created=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    encargado = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    contenido = models.TextField()
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.CASCADE)
    fecha = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    fecha_fin = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    hora = models.TimeField(
        auto_now=False, auto_now_add=False, default=datetime.datetime.now().time())
    duracion = models.ForeignKey(Duracion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.nombre}'


class ArchivosCapacitacion(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)
    capacitacion = models.ForeignKey(Capacitaciones, on_delete=models.CASCADE)
    file = FileField(upload_to=create_path_capacitaciones)

    def __str__(self):
        return f'{self.id} {self.file}'

    def filename(self):
        return os.path.basename(self.file.name)


class Invitados(models.Model):
    id = models.AutoField(primary_key=True)
    capacitacion = models.ForeignKey(Capacitaciones, on_delete=models.CASCADE)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.rut} {self.nombre}'


class Hito(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = DateTimeField(auto_created=True, auto_now=True)
    fecha = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    capacitacion = models.ForeignKey(Capacitaciones, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'


class HitoAsistencia(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = DateTimeField(auto_created=True, auto_now=True)
    hito = models.ForeignKey(
        Hito, on_delete=models.CASCADE, related_name='asist')
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class ArchivosHitos(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)
    hito = models.ForeignKey(
        Hito, on_delete=models.CASCADE, related_name='hito_archivos')
    file = FileField(upload_to=create_path_hito)

    def __str__(self):
        return f'{self.id} {self.file}'

    def filename(self):
        return os.path.basename(self.file.name)
