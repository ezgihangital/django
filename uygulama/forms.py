from django import forms
from uygulama.models import uygulama

class UygulamaForm(forms.ModelForm):
    class Meta:
        model = uygulama
        fields= [
            'title',
        ]