from .models import Plant_Details
from django import forms
class PlantDetailsForm(forms.ModelForm):
    class Meta:
        model=Plant_Details
        fields="__all__"
