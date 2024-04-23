from django.contrib.auth.models import User
from django.db import models

FUEL_TYPES = {
    'Gasolina Especial': 'Gasolina Especial',
    'Gasolina Etanol': 'Gasolina Etanol',
    'Gasolina Premium': 'Gasolina Premium',
}


class VehicleType(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Tipo de Vehiculo'
        verbose_name_plural = 'Tipos de Vehiculos'


class Vehicle(models.Model):
    user = models.ForeignKey(User, null=True, related_name='vehicles', on_delete=models.CASCADE, verbose_name='Usuario')
    brand = models.CharField(default='', max_length=250, verbose_name='Marca')
    model = models.CharField(default='', max_length=250, verbose_name='Modelo')
    year = models.CharField(default=0, max_length=4, verbose_name='Año')
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicles', on_delete=models.CASCADE, verbose_name='Tipo de Vehiculo')
    plate = models.CharField(max_length=200, unique=True, verbose_name='Placa')

    @property
    def distance(self):
        fuel_loads = self.fuel_loads.all()
        count = len(fuel_loads)
        result = 0
        if count > 0:
            last = fuel_loads[0]
            first = fuel_loads[count - 1]
            result = round(last.odometer - first.odometer)
        return result

    @property
    def odometer(self):
        loads = self.fuel_loads.all()
        count = len(loads)
        if count > 0:
            last = loads[0]
            return round(last.odometer)
        return 0

    @property
    def spent(self):
        loads = self.fuel_loads.all()
        result = 0
        for load in loads:
            result += (load.liters * load.fuel_type.price)
        return round(result)

    @property
    def liters(self):
        loads = self.fuel_loads.all()
        result = 0
        for load in loads:
            result += load.liters
        return round(result)

    def __str__(self) -> str:
        return self.plate

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'


class FuelType(models.Model):
    name = models.CharField(choices=FUEL_TYPES, max_length=200, verbose_name='Nombre')
    price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Precio por litro')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')

    def __str__(self) -> str:
        return self.get_name_display()

    class Meta:
        verbose_name = 'Tipo de Combustible'
        verbose_name_plural = 'Tipos de Combustible'
        ordering = ['pk']


class Fueling(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True, related_name='fuel_loads', on_delete=models.CASCADE, verbose_name='Vehiculo')
    user = models.ForeignKey(User, related_name='fuel_loads', on_delete=models.CASCADE, verbose_name='Usuario')
    fuel_type = models.ForeignKey(FuelType, related_name='fuel_loads', on_delete=models.CASCADE, verbose_name='Tipo de Combustible')
    upload_date = models.DateTimeField(verbose_name='Fecha de Carga')
    liters = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Litros')
    odometer = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Odometro')

    def __str__(self) -> str:
        return f'{self.fuel_type.name} - {self.liters}'

    @property
    def total(self) -> float:
        return round(self.fuel_type.price * self.liters, 2)

    class Meta:
        verbose_name = 'Carga de Combustible'
        verbose_name_plural = 'Cargas de Combustible'
