from django import forms
from .models import Ruta

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
