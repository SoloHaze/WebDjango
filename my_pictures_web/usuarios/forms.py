from django import forms

class PintorForm(forms.Form):
    firstname = forms.CharField(max_length=50,min_length=3)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    joined_date = forms.DateField()
    password = forms.CharField(max_length=8)
    repeatPass = forms.CharField()
    


class PinturaForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    tecnicaUsada = forms.CharField(max_length=20)
    imagen = forms.FileField(required=False)


class LoginForm(forms.Form):
    email= forms.EmailField()
    password= forms.CharField(max_length=8)


class RegistroForm(forms.Form):
    firstname = forms.CharField(max_length=50,min_length=3)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    joined_date = forms.DateField()
    password = forms.CharField(max_length=8)
    repeatPass = forms.CharField()
    tipoUsuario= forms.CharField(max_length=20)
    