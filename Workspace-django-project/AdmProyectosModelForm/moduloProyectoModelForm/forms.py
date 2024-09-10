from django import forms
from moduloProyectoModelForm.models import Proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
