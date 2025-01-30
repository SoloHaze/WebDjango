from django import forms
from .models import Pintura, Contacto


class PintorForm(forms.Form):
    firstname = forms.CharField(max_length=50,min_length=3)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    password = forms.CharField(max_length=8,widget=forms.PasswordInput())
    repeatPass = forms.CharField(widget=forms.PasswordInput())
    

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje']

class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ['nombre','descripcion','precio','tecnicaUsada','imagen']


class LoginForm(forms.Form):
    email= forms.EmailField()
    password= forms.CharField(max_length=8,widget=forms.PasswordInput())


class RegistroForm(forms.Form):
    firstname = forms.CharField(max_length=50,min_length=3)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    password = forms.CharField(max_length=8,widget=forms.PasswordInput())
    repeatPass = forms.CharField(widget=forms.PasswordInput())
    tipoUsuario= forms.CharField(max_length=20)
    