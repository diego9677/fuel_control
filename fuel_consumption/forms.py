from django import forms
from .models import Fueling


class FuelingForm(forms.ModelForm):
    class Meta:
        model = Fueling
        fields = ['fuel_type', 'upload_date', 'unit_price', 'liters', 'total']
        widgets = {
            'upload_date': forms.TextInput(attrs={'type': 'datetime-local'})
        }
