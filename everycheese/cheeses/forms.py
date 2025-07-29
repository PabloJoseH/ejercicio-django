from django import forms
from django_countries.fields import CountryField
from .models import Cheese

class AddCheeseForm(forms.ModelForm):
    country = CountryField().formfield(blank_label="(selecciona país)")

    class Meta:
        model  = Cheese
        fields = ["name", "description", "firmness", "country"]
