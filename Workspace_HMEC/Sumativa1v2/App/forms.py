from django import forms
from .models import Reserva, EstadReserva, TipoReserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre',
            'telefono',
            'fecha_nacimiento',
            'fechareserva',
            'horareserva',
            'cantidad_hermanos',
            'foto_carnet',
            'observaciones',
            'website',
            'email',
            'estadoReservaId',
            'tipoSolicitudId'
        ]

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha de Nacimiento'
    )
    fechareserva = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
        label='Fecha Reserva'
    )
    horareserva = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}), 
        label='Hora Reserva'
    )
    cantidad_hermanos = forms.IntegerField(
        label='Cantidad de Hermanos',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    foto_carnet = forms.ImageField(
        required=False, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Archivo a Subir'
    )
    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'form-control'}),
        label='Observaciones'
    )
    website = forms.URLField(
        label='Sitio Web',
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    estadoReservaId = forms.ModelChoiceField(
        queryset=EstadReserva.objects.all(), 
        label='Estado Reserva',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tipoSolicitudId = forms.ModelChoiceField(
        queryset=TipoReserva.objects.all(), 
        label='Tipo Reserva',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Validaciones personalizadas
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) <= 2:
            raise forms.ValidationError("El nombre debe tener más de dos letras.")
        return nombre

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get('observaciones')
        palabras = observaciones.split()
        if len(palabras) < 5:
            raise forms.ValidationError("Las observaciones deben contener al menos 5 palabras.")
        return observaciones
