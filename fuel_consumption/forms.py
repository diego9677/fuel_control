from django import forms
from .models import Fueling, Vehicle


class FuelingForm(forms.ModelForm):

    class Meta:
        model = Fueling
        fields = ['vehicle', 'fuel_type', 'upload_date', 'liters', 'odometer']
        widgets = {
            'upload_date': forms.TextInput(attrs={'type': 'datetime-local'})
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate', 'vehicle_type']
