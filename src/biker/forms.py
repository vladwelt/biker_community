from django import forms
from .models import Evento, Grupo, Ruta

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre','punto_partida','fecha','ruta','grupo']

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'
