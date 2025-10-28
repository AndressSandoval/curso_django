from django.contrib import admin
from .models import Sucursal, Empleado

# Permite añadir empleados directamente al crear/editar una sucursal
class EmpleadoInline(admin.TabularInline):
    model = Empleado
    extra = 1  # Muestra 1 formulario vacío por defecto

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'ciudad', 'pais', 'calle')
    inlines = [EmpleadoInline]

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'cargo', 'sucursal', 'salario', 'fecha_contratacion')
    list_filter = ('sucursal', 'cargo')