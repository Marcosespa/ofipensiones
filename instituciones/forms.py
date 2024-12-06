from django import forms
from .models import Institucion, Servicio, Curso

class InstitucionForm(forms.ModelForm):
    """Formulario para crear o actualizar instituciones."""
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono', 'email_contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email_contacto': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ServicioForm(forms.ModelForm):
    """Formulario para crear o actualizar servicios."""
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'costo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    """Formulario para crear o actualizar cursos."""
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion_semanas', 'fecha_inicio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion_semanas': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
