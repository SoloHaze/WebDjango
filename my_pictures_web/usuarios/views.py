from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from .models import Pintor,Pintura, Contacto
from .forms import PintorForm, PinturaForm, LoginForm, RegistroForm, ContactoForm
from django.views.decorators.csrf import csrf_protect
from datetime import date
from django.contrib import messages
from django.contrib.auth.hashers import check_password


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
   pinturas = Pintura.objects.all()
   return render(request,'index.html',{'request': request, 'dolar': valor_dolar, 'pinturas': pinturas})

def pintores(request):
  pintores = Pintor.objects.all().values()
  template = loader.get_template('todosLosPintores.html')
  context = {
    'pintores': pintores,
  }
  return HttpResponse(template.render(context, request))


def contacto(request):
    template = loader.get_template('contacto.html')
    if request.method=="GET":
            form = ContactoForm(request.GET)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                email = form.cleaned_data['email']
                mensaje = form.cleaned_data['mensaje']
                contacto = Contacto(nombre = nombre, email= email, mensaje=mensaje)
                contacto.save()
                return redirect('contacto') 
            else:
                form = RegistroForm()
                context = {'form': form}        
            return HttpResponse(template.render(context,request))            
                               
    return HttpResponse(template.render(context,request))


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
def pinturasPintor(request):
    pinturas = Pintura.objects.all()

    return render(request, 'todasLasPinturas.html', {'pinturas': pinturas})    

@requiere_usuario('pintor')
def crear_pintura(request):
   if request.method=="POST":
        form = PinturaForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('planillaPinturasDina')
   else:
      form = PinturaForm()
   return render(request, 'agregarPintura.html', {'form': form})
   

def planillaPinturas(request):
      pinturas = Pintura.objects.all()
      #template = loader.get_template('planillaPinturasDina.html')
      #context ={
      #      'pinturas': pinturas
      #   }
      return render(request, 'planillaPinturasDina.html', {'pinturas': pinturas})

def planillaPinturasAdmin(request):
    pinturas = Pintura.objects.all()
    return render(request, 'planillaPinturasDina.html', {'pinturas': pinturas})

@requiere_usuario('admin')
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

def registroAdmin(request):
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


def loginAdmin(request):
    template = loader.get_template('loginAdmin.html')
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['email']
            clave = form.cleaned_data['password']
            try:
                usuarioLogueado = Pintor.objects.get(email=correo)
                if check_password(clave, usuarioLogueado.password):
                    request.session['usuario_id'] = usuarioLogueado.id
                    request.session['usuarioTipo'] = usuarioLogueado.tipoUsuario
                    request.session['usuarioFirstName'] = usuarioLogueado.firstname
                    return redirect('main')
                else:
                    messages.error(request, "La contraseña es incorrecta.")
            except Pintor.DoesNotExist:
                messages.error(request, "No se encontró un usuario con ese correo.")
            except Exception as e:
                messages.error(request, f"Hubo un error inesperado: {str(e)}")

    return HttpResponse(template.render(context, request))


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

@requiere_usuario('admin')
def actualizar_estado(request, id):
    # Verificamos si el usuario es un administrador
    if request.user.tipoUsuario != "admin":
        return HttpResponseForbidden("No tienes permisos para realizar esta acción.")

    # Recuperamos la pintura
    pintura = Pintura.objects.get(id=id)

    if request.method == 'POST':
        razon = request.POST.get('razon', '')
        accion = request.POST.get('accion')
        
        # Si la acción es aprobar
        if accion == 'aprobar':
            pintura.aprobado = True
        # Si la acción es rechazar
        elif accion == 'rechazar':
            pintura.aprobado = False

        # Guardamos la razón proporcionada por el admin
        pintura.razon = razon
        pintura.save()

        # Mensaje de éxito
        messages.success(request, f'Pintura {accion}da correctamente.')

        return redirect('planillaPinturasAdmin')

    return redirect('planillaPinturasAdmin')