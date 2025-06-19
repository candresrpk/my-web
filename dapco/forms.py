from django import forms
from .models import Encuesta, Pregunta, Opcion, Respuesta, Distribucion, Usuario
from django.contrib.auth.models import User


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['encuesta', 'status']
    
    def __init__(self, *args, **kwargs):
        super(EncuestaForm, self).__init__(*args, **kwargs)
        self.fields['encuesta'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
    
    
    