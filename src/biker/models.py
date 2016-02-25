from django.db import models
from django.contrib.auth.models import User

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    grupo = models.ForeignKey(Grupo)
    user = models.ForeignKey(User, null=True) 

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    distancia = models.FloatField()
    usuario = models.ForeignKey(Usuario)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    punto_partida = models.CharField(max_length=100)
    fecha = models.DateField()
    ruta = models.ForeignKey(Ruta)
    grupo = models.ManyToManyField(Grupo, related_name = 'users', default = None)

    def __str__(self):
        return self.nombre
# Create your models here.
