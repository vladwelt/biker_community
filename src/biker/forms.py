from django import forms
from .models import Evento, Grupo

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre','punto_partida','fecha','ruta','grupo']

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
