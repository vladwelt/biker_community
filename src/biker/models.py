from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

class User(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    grupo = models.ForeignKey(Grupo)

class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    distancia = models.FloatField()
    usuario = models.ForeignKey(User)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    punto_partida = models.CharField(max_length=100)
    fecha = models.DateField()
    ruta = models.ForeignKey(Ruta)
    grupo = models.ForeignKey(Grupo)

# Create your models here.
