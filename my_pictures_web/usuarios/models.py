from django.db import models

# Create your models here.


class Pintor(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  password = models.CharField(max_length=8)
  tipoUsuario = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('pintor', 'pintor')], default='pintor')



class Contacto(models.Model):
   nombre = models.CharField(max_length=50)
   email = models.EmailField()
   mensaje = models.CharField(max_length=3000)


class Pintura(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    autor = models.CharField(max_length=30,null=True)
    tecnicaUsada = models.CharField(max_length=20)
    fechaSubida = models.DateField(null=True)
    estado = models.CharField(max_length=10,null=True)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
       return self.nombre
