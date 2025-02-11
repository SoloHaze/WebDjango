from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from .models import Pintor,Pintura, Contacto
from .forms import PintorForm, PinturaForm, LoginForm, RegistroForm, ContactoForm
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
   pinturas = Pintura.objects.all()
   pintores = Pintor.objects.all()
   return render(request,'index.html',{'request': request, 'dolar': valor_dolar, 'pinturas': pinturas, 'pintores': pintores})


@requiere_usuario('admin')
def pintores(request):
  pintores = Pintor.objects.all().values()
  template = loader.get_template('todosLosPintores.html')
  context = {
    'pintores': pintores,
  }
  return HttpResponse(template.render(context, request))


def contacto(request):
    if request.method == "GET":
        form = ContactoForm()  # Crea un formulario vacío si es un GET
    elif request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
            contacto.save()

            return redirect('contacto')  # O puedes redirigir a otra página después de guardar, como la misma vista

    context = {'form': form}  # Asegúrate de siempre pasar un contexto
    return render(request, 'contacto.html', context)


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
               
               return redirect('login')
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

    return render(request,'detallePintura.html',{'pintura': pintura})

@requiere_usuario('pintor')
def pinturasPintor(request):
    pinturas = Pintura.objects.all()

    return render(request, 'todasLasPinturas.html', {'pinturas': pinturas})    





@requiere_usuario('pintor')
def crear_pintura(request):
   if request.method=="POST":
        form = PinturaForm(request.POST, request.FILES)
        if form.is_valid():
            
               nombre = form.cleaned_data['nombre']
               descripcion = form.cleaned_data['descripcion']
               precio = form.cleaned_data['precio']

               usuario_id = request.session.get('usuario_id')
               if usuario_id is None:
                return redirect('login')
               usuarioLogueado = Pintor.objects.get(id=usuario_id)


               autor = usuarioLogueado.firstname
               tecnicaUsada = form.cleaned_data['tecnicaUsada']
               fechaSubida = date.today()
               estado = "en revision"
               imagen = form.cleaned_data['imagen']
            
               pintura = Pintura(nombre=nombre, descripcion=descripcion, precio=precio, autor=autor, tecnicaUsada=tecnicaUsada,fechaSubida=fechaSubida, estado=estado, imagen=imagen)
                    
               pintura.save()
 
               return redirect('planillaPinturasDina')
   else:
      form = PinturaForm()
   return render(request, 'agregarPintura.html', {'form': form})
   
def get_total(self):
    return Pintura.objects.count()
    


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
               request.session['firstname'] = pintor.firstname
               return redirect('login')
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
               
               return redirect('login')
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
def lista_pinturas(request):
    # obtiene todas las pinturas
    pinturas = Pintura.objects.all()

    if request.method == 'POST':
       
        pintura_id = request.POST.get('pintura_id')
        estado = request.POST.get('estado')

        pintura = get_object_or_404(Pintura, id=pintura_id)
        if estado in ['aprobado', 'reprobado']:
            pintura.estado = estado
            pintura.save()
     
            return redirect('planillaPinturasAdmin')  

    return render(request, 'planillaPinturasAdmin.html', {'pinturas': pinturas})


def pinturas_pintor(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id is None:
        return redirect('login')  #verifica si no hay un usuario logueado

    pinturas = Pintura.objects.filter(id=usuario_id, estado="aprobado")

    return render(request, 'misPinturasAprobadas.html', {'pinturas': pinturas})
    

def mis_pinturas(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id is None:
        return redirect('login')  #verifica si no hay un usuario logueado

    # Obtener todas las pinturas del pintor en la sesión actual
    pinturas = Pintura.objects.filter(id=usuario_id)

    return render(request, 'misPinturas.html', {'pinturas': pinturas})
