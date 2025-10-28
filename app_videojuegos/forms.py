from django import forms
from .models import Sucursal, Empleado
from django.forms import inlineformset_factory

# Formulario para el modelo Sucursal
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        # Campos del modelo Sucursal que se mostrarán en el formulario
        fields = ['direccion', 'ciudad', 'pais', 'calle', 'codigo_postal', 'foto_sucursal']

# Formulario personalizado para Empleado
class EmpleadoForm(forms.ModelForm):
    fecha_contratacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Empleado
        fields = ['apellido', 'fecha_contratacion', 'cargo', 'salario', 'foto_empleado']

# FormSet para el modelo Empleado
EmpleadoFormSet = inlineformset_factory(
    Sucursal,  # Modelo padre
    Empleado,  # Modelo hijo
    form=EmpleadoForm,
    extra=1,         # Cuántos formularios extra mostrar
    can_delete=True  # Permitir borrar empleados desde el formset
)
