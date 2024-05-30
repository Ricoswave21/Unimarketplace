from django import forms
from .models import Items
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewitemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields=("category","name","description","price","image",)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }




class EmailForm(forms.Form):
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'class': INPUT_CLASSES
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': INPUT_CLASSES
    }), required=False)  # Optional phone number field
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',
        'class': INPUT_CLASSES
    }), required=False)  # Optional address field