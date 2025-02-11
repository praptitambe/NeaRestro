from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = [
            'name', 'email', 'restro_name', 'description',
            'address_line1', 'address_line2', 'city', 'postcode',
            'cuisine_type', 'restro_image'
        ]
