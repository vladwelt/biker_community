from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    imagen = models.FileField(null=True, upload_to='grupos/%Y%m%d_%H-%M-%s')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    grupo = models.ForeignKey(Grupo)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    foto = models.FileField(null=True, upload_to='users/%Y%m%d_%H-%M-%s')

    def __unicode__(self):
        return unicode(self.user)

class Ruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    distancia = models.FloatField()
    descripcion = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True)
    imagen = models.FileField(null=True, upload_to='rutas/%Y%m%d_%H-%M-%s')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('route-detail', kwargs={'pk': self.pk})

class Evento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    punto_partida = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    ruta = models.ForeignKey(Ruta)
    grupo = models.ManyToManyField(Grupo, related_name = 'users', default = None)
    imagen = models.FileField(null=True, upload_to='eventos/%Y%m%d_%H-%M-%s')

    def __str__(self):
        return self.nombre
# Create your models here.
