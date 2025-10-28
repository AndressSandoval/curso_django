from django.db import models
from django.urls import reverse

# Modelo Principal (como 'Artista' en el original)
class Sucursal(models.Model):
    # Campos que pediste
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    calle = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=20)
    
    # Campo añadido para mantener la funcionalidad visual del original
    foto_sucursal = models.ImageField(upload_to='fotos_sucursales/', blank=True, null=True)

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}"

    def get_absolute_url(self):
        # Apunta a la URL de detalle de la sucursal
        return reverse('app_videojuegos:detalle_sucursal', kwargs={'pk': self.pk})

# Modelo Relacionado (como 'Cancion' en el original)
class Empleado(models.Model):
    # Campos que pediste
    apellido = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    # Campo para foto del empleado
    foto_empleado = models.ImageField(upload_to='fotos_empleados/', blank=True, null=True)

    # Clave foránea que lo relaciona con Sucursal
    sucursal = models.ForeignKey(Sucursal, related_name='empleados', on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido
