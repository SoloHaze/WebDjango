from django.db import models

# Create your models here.


class Pintor(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  password = models.CharField(max_length=8)
  tipoUsuario = models.CharField(max_length=15)



class Pintura(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    autor = models.CharField(max_length=30)
    tecnicaUsada = models.CharField(max_length=20)
    fechaSubida = models.DateField()
    estado = models.CharField(max_length=10)
    imagen = models.FileField(null=False)