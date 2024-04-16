# Generated by Django 5.0.4 on 2024-04-16 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_consumption', '0003_vehicle_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=200, unique=True, verbose_name='Placa'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='fuel_consumption.vehicletype', verbose_name='Tipo de Vehiculo'),
        ),
    ]