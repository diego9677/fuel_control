from django import forms
from .models import Fueling


class FuelingForm(forms.ModelForm):

    class Meta:
        model = Fueling
        fields = ['fuel_type', 'upload_date', 'liters', 'odometer']
        widgets = {
            'upload_date': forms.TextInput(attrs={'type': 'datetime-local'})
        }
