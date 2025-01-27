from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Pintor,Pintura
from .forms import PintorForm, PinturaForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def main(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())

def pintores(request):
  pintores = Pintor.objects.all().values()
  template = loader.get_template('todosLosPintores.html')
  context = {
    'pintores': pintores,
  }
  return HttpResponse(template.render(context, request))


def detalles(request, id):
    pintor = Pintor.objects.get(id=id)
    template = loader.get_template('detalles.html')
    context ={
       'pintor':pintor
    }
    return HttpResponse(template.render(context,request))

def crear_pintor(request):
   template = loader.get_template("formulario-pintores.html")
   
   if request.method=="GET":
        form = PintorForm(request.GET)
        if form.is_valid():
           firstname = form.cleaned_data['firstname']
           lastname = form.cleaned_data['lastname']
           email = form.cleaned_data['email']
           phone = form.cleaned_data['phone']
           joined_date = form.cleaned_data['joined_date']
           
           Pintor.objects.all()
           pintor = Pintor(firstname=firstname, lastname=lastname, email=email, phone=phone, joined_date=joined_date)
           pintor.save()
           
           return redirect('usuarios')
        else:
           form = PintorForm()
           context = {'form': form}
           return HttpResponse(template.render(context,request))
   else:


      form = PintorForm()
      context = {'form': form}

      return HttpResponse(template.render(context,request))
   
def detallePintura(request, id):
    pintura = Pintura.objects.get(id=id)
    template = loader.get_template('detallePintura.html')
    context ={
       'pintura':pintura
    }
    return HttpResponse(template.render(context,request))

@csrf_protect
def crear_pintura(request):
   template = loader.get_template("agregarPintura.html")
   
   if request.method=="POST":
        form = PinturaForm(request.POST)
        if form.is_valid():
           nombre = form.cleaned_data['nombre']
           descripcion = form.cleaned_data['descripcion']
           precio = form.cleaned_data['precio']
           tecnicaUsada = form.cleaned_data['tecnicaUsada']
           fechaSubida = form.cleaned_data['fechaSubida']
           estado = form.cleaned_data['estado']
           imagen = form.cleaned_data['imagen']


           Pintura.objects.all()
           pintura = Pintura(nombre=nombre, descripcion=descripcion, precio=precio, tecnicaUsada=tecnicaUsada, fechaSubida=fechaSubida, estado= estado, imagen= imagen)
           pintura.save()
           
           return redirect('pinturas')
        else:
           form = PinturaForm()
           context = {'form': form}
           return HttpResponse(template.render(context,request))
   else:


      form = PinturaForm()
      context = {'form': form}

      return HttpResponse(template.render(context,request))
   

def planillaPinturas(request):
      pintura = Pintura.objects.all().values()
      template = loader.get_template('planillaPinturasDina.html')
      context ={
            'pintura':pintura
         }
      return HttpResponse(template.render(context,request))