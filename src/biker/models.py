import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    foto = models.FileField(null=True, upload_to='users/%Y%m%d_%H-%M-%s')

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    administrador = models.ForeignKey(Usuario, null=True)
    imagen = models.FileField(null=True, upload_to='grupos/%Y%m%d_%H-%M-%s')
    usuarios = models.ManyToManyField(Usuario, related_name = 'grupos', default = None)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

class Ruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    distancia = models.PositiveIntegerField()
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

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

class Solicitud(models.Model):
    STATE_CHOICES = (
            ('A', 'Approved'),
            ('R', 'Rejected'),
            ('P', 'Pending'),
        )
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(Usuario)
    group = models.ForeignKey(Grupo)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='P')
    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    accepted_date = models.DateTimeField(null=True)

    def is_approved(self):
        return self.state == 'A'

    def accepted(self):
        self.state = 'A'
        self.accepted_date = datetime.datetime.now()
        self.save()

    def save(self, *args, **kwargs):
        self.name = 'user_'+ str(self.user.pk) + '_group_' + str(self.group.pk)
        super(Solicitud, self).save(*args, **kwargs)
