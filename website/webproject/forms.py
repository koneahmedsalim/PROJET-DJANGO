from django import forms
from .models import Client

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}
