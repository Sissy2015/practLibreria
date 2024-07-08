from django import forms
from .models import categoria
class CategoriaForms(forms.ModelForm):
    class Meta:
     model=categoria
     fields=['nombre']
