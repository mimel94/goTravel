from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
            

class controlUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(controlUsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
           'class': 'form-control',
           'placeholder':'Ingrese la contraseña',
           'required':'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
           'class': 'form-control',
           'placeholder':'Ingrese nuevamente la contraseña ',
           'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','email','tipo_documento','numero_documento','nombre','apellidos','edad','ocupacion')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user