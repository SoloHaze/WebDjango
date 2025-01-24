from django import forms

class PintorForm(forms.Form):
    firstname = forms.CharField(max_length=50,min_length=3)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    joined_date = forms.DateField()


class PinturaForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    autor = forms.CharField(max_length=30)
    tecnicaUsada = forms.CharField(max_length=20)
    fechaSubida = forms.DateField()
    estado = forms.CharField(max_length=10)
    imagen = forms.FileField()