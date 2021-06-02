from django import forms

from .models import Drink


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = (
            'name',
            'quantity',
            'price',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Vodka',
                    'required': True,
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '1',
                    'required': True,
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '100.0',
                    'required': True,
                }
            ),
        }
