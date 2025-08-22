# flights/forms.py
from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['nombre', 'tipo', 'precio'] # Los campos que queremos mostrar
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Rionegro - Bogotá', 'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'step': '1000', 'min': '0', 'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }   