from django import forms
from .models import Peliculas


class peliculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['titulo','reseña', 'imagen', 'favorita']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe un titulo'}),
            'reseña': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'escribe una reseña'}),
            'favoritas': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }