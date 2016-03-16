from django import forms
from .models import Ruta, Grupo, Solicitud

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['nombre','distancia','descripcion','imagen']
    
    def clean_distancia(self):
        distancia_limpia = self.cleaned_data
        distancia = distancia_limpia.get('distancia')
        if distancia<0:
           raise forms.ValidationError("La distancia debe ser mayor a 0")
        return distancia

class EventoSearchForm(forms.Form):
    nombre_evento=forms.CharField(label='Nombre del evento a buscar',max_length=50)

class GrupoSearchForm(forms.Form):
    nombre_grupo=forms.CharField(label='Nombre del grupo a buscar',max_length=50)

class RutaSearchForm(forms.Form):
    nombre_ruta=forms.CharField(label='Nombre de la ruta a buscar',max_length=50)

class SolicitudForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Grupo.objects.all(),widget=forms.HiddenInput())

    class Meta:
        model = Solicitud
        fields = ['group']
