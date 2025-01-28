from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Pintor,Pintura
from .forms import PintorForm, PinturaForm, LoginForm, RegistroForm
from django.views.decorators.csrf import csrf_protect
from datetime import date
# Create your views here.
#decorador validador de rutas:
def requiere_usuario(tipo_requerido):
   def decorator(func):
       def wrapper(request, *args, **kwargs):
           if 'usuarioTipo' not in request.session or request.session['usuarioTipo'] != tipo_requerido:
               return redirect('main')
           return func(request, *args, **kwargs)
       return wrapper
   return decorator


import requests
def main(request):
   r = requests.get('https://mindicador.cl/api')
   valor_dolar= r.json()['dolar']['valor']
   return render  (request,'index.html',{'request': request, 'dolar': valor_dolar})

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

@requiere_usuario('admin')
def crear_pintor(request):
   template = loader.get_template("formulario-pintores.html")
   
   if request.method=="GET":
        form = PintorForm(request.GET)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            joined_date = date.today()
            password = form.cleaned_data['password']
            repeatPass = form.cleaned_data['repeatPass']
            tipoUsuario = "pintor"
            if password!=repeatPass:
               
               form = PintorForm()
               context = {'form': form}
               
               return HttpResponse(template.render(context,request))   
            else:    

               pintor = Pintor(firstname=firstname, lastname=lastname, email=email, phone=phone, joined_date=joined_date,password=repeatPass, tipoUsuario=tipoUsuario)
               pintor.save()
               
               return redirect('pintores')
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

@requiere_usuario('pintor')
def crear_pintura(request):
   template = loader.get_template("agregarPintura.html")
   
   if request.method=="GET":
        form = PinturaForm(request.GET)
        if form.is_valid():
           nombre = form.cleaned_data['nombre']
           descripcion = form.cleaned_data['descripcion']
           precio = form.cleaned_data['precio']
           autor = request.session['usuarioFirstName']
           tecnicaUsada = form.cleaned_data['tecnicaUsada']
           fechaSubida = date.today()
           estado = 'en espera'
           imagen = form.cleaned_data['imagen']


           pintura = Pintura(nombre=nombre, descripcion=descripcion, precio=precio,autor= autor, tecnicaUsada=tecnicaUsada, fechaSubida=fechaSubida, estado= estado, imagen= imagen)
           pintura.save()
           
           return redirect('planillaPinturasDina')
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
            'pintura': pintura
         }
      return HttpResponse(template.render(context,request))


def registro(request):
   template = loader.get_template("registro.html")
   
   if request.method=="GET":
        form = RegistroForm(request.GET)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            joined_date = date.today()
            password = form.cleaned_data['password']
            repeatPass = form.cleaned_data['repeatPass']
            tipoUsuario = form.cleaned_data['tipoUsuario']
            if password!=repeatPass:
               
               form = RegistroForm()
               context = {'form': form}
               
               return HttpResponse(template.render(context,request))   
            else:    

               pintor = Pintor(firstname=firstname, lastname=lastname, email=email, phone=phone, joined_date=joined_date,password=repeatPass, tipoUsuario=tipoUsuario)
               pintor.save()
               
               return redirect('loginn')
        else:
           form = RegistroForm()
           context = {'form': form}
           return HttpResponse(template.render(context,request))
   else:


      form = RegistroForm()
      context = {'form': form}

      return HttpResponse(template.render(context,request))


def login(request):
    template = loader.get_template('login.html')
    form = LoginForm()
    context = {'form': form}
    return HttpResponse(template.render(context,request))


def loginn(request):
    template = loader.get_template('loginn.html')
    form = LoginForm()
    context = {'form': form}
    if request.method=='GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            try:
                correo = form.cleaned_data['email']
                clave = form.cleaned_data['password']

                usuarioLogueado = Pintor.objects.get(email=correo,password=clave)
                request.session['usuario_id'] = usuarioLogueado.id
                request.session['usuarioTipo'] = usuarioLogueado.tipoUsuario
                request.session['usuarioFirstName'] = usuarioLogueado.firstname
                return redirect('main')
            except:
                #Aqui deberian mostrar un mensaje de error:
                pass

    return HttpResponse(template.render(context,request))

def logout(request):
   request.session.flush()
   return redirect('main')


