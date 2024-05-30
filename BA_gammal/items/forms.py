from django import forms
from .models import Items


class NewitemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields=("category","name","description","price","image",)

