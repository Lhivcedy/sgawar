from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import FileField

# importar el modelo de tabla de usuario desde el administrador
from django.contrib.auth.models import User
# importar libreria de autentificacion
from django.contrib.auth import authenticate, logout, login as login_aut
# importar libreria decoradora que evita el ingreso a las paginas sin autorizacion
from django.contrib.auth.decorators import login_required,permission_required

# Create your models here.
class Tema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=1000)
    
    def __str__(self):
        return f'{self.id} {self.nombre}'
   
class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)
    file = FileField(upload_to='archivos')
    tema = models.ForeignKey(Tema,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.file}'