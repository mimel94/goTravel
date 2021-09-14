from django import forms
from django.forms import fields
from .models import sitio

class SitioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SitioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                    'class': 'form-control'
                }
    class Meta:
        model = sitio
        fields = ('nombre', 'ciudad', 'descripcion', 'album_url', 'ubicacion')