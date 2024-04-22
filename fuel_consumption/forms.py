from django import forms
from .models import Fueling, Vehicle


class FuelingForm(forms.ModelForm):
    class Meta:
        model = Fueling
        fields = ['vehicle', 'fuel_type', 'upload_date', 'liters', 'odometer']
        widgets = {
            'upload_date': forms.TextInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FuelingForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(user=user).all()


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate', 'vehicle_type']
