from django import forms
from .models import Vehiculo
import re

class VehiculoForm(forms.ModelForm):
    # Dividimos la patente en dos partes en el formulario
    patente_numero = forms.CharField(
        max_length=6, 
        min_length=6,  # Limitar a exactamente 6 caracteres
        label='Patente (número)', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '')", 'required': True})
    )
    patente_dv = forms.CharField(
        max_length=1, 
        min_length=1,  # Limitar a exactamente 1 carácter
        label='Patente (DV)', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '')", 'required': True})
    )

    class Meta:
        model = Vehiculo
        fields = ['nro_chasis', 'nro_motor', 'modelo', 'fecha_vencimiento', 'tipo_vehiculo', 'marca', 'posee_seguro', 'observaciones']
        widgets = {
            'nro_chasis': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12', 'minlength': '12', 'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '')", 'required': True}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '17', 'minlength': '17', 'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '')", 'required': True}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'posee_seguro': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')]),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }

    # Validaciones para patente
    def clean_patente_numero(self):
        patente_numero = self.cleaned_data.get('patente_numero')
        if len(patente_numero) != 6:
            raise forms.ValidationError("La patente debe contener 6 caracteres alfanuméricos.")
        return patente_numero

    def clean_patente_dv(self):
        patente_dv = self.cleaned_data.get('patente_dv')
        if len(patente_dv) != 1:
            raise forms.ValidationError("El dígito verificador debe contener 1 carácter.")
        return patente_dv

    # Validaciones adicionales para chasis y motor
    def clean_nro_chasis(self):
        nro_chasis = self.cleaned_data.get('nro_chasis').replace(" ", "").upper()
        if len(nro_chasis) != 12:
            raise forms.ValidationError("El número de chasis debe tener exactamente 12 caracteres.")
        return nro_chasis

    def clean_nro_motor(self):
        nro_motor = self.cleaned_data.get('nro_motor').replace(" ", "").upper()
        if len(nro_motor) != 17:
            raise forms.ValidationError("El número de motor debe tener exactamente 17 caracteres.")
        return nro_motor

    # Combinamos los campos patente_numero y patente_dv
    def clean(self):
        cleaned_data = super().clean()
        patente_numero = cleaned_data.get('patente_numero')
        patente_dv = cleaned_data.get('patente_dv')
        
        # Combinamos el número de la patente y el dígito verificador
        if patente_numero and patente_dv:
            cleaned_data['patente'] = f"{patente_numero}-{patente_dv}"

        return cleaned_data
