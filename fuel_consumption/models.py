from django.contrib.auth.models import User
from django.db import models

FUEL_TYPES = {
    'special': 'Gasolina Especial',
    'ethanol': 'Gasolina Etanol'
}


class FuelType(models.Model):
    name = models.CharField(choices=FUEL_TYPES, max_length=200, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self) -> str:
        return self.get_name_display()

    class Meta:
        verbose_name = 'Tipo de Combustible'
        verbose_name_plural = 'Tipos de Combustible'


class Fueling(models.Model):
    user = models.ForeignKey(User, related_name='fuel_loads', on_delete=models.CASCADE, verbose_name='Usuario')
    fuel_type = models.ForeignKey(FuelType, related_name='fuel_loads', on_delete=models.CASCADE, verbose_name='Tipo de Combustible')
    upload_date = models.DateTimeField(verbose_name='Fecha de Carga')
    unit_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio unitario')
    liters = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Litros')
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self) -> str:
        return f'{self.fuel_type.name} - {self.liters}'

    class Meta:
        verbose_name = 'Carga de Combustible'
        verbose_name_plural = 'Cargas de Combustible'
