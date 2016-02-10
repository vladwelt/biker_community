from django import forms
from .models import Evento, Grupo, Ruta

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre','punto_partida','fecha','ruta','grupo']
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['ruta'].widget.attrs.update({'class' : 'form-control'})
        self.fields['grupo'].widget.attrs.update({'class' : 'form-control','multiple':''})

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RutaForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs.update({'class' : 'form-control'})
