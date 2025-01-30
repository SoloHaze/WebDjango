from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.main,name="main"),
    path('pintores/', views.pintores, name="pintores" ),
    path('pintores/detalles/<int:id>', views.detalles, name="detalles" ),
    path('crear-pintor', views.crear_pintor, name="crear_pintor" ),
    path('crear-pintura', views.crear_pintura, name="crear_pintura" ),
    path('detallePintura/<int:id>', views.detallePintura, name="detallePintura" ),
    path('planillaPinturasDina', views.planillaPinturas, name="planillaPinturasDina" ),
    path('login', views.login, name="login" ),
    path('logout', views.logout, name="logout" ),
    path('contacto', views.contacto, name="contacto" ),
    path('registroAdmin', views.registroAdmin, name="registroAdmin" ),
    path('registro', views.registro, name="registro" ),
    path('planillaPinturasAdmin', views.lista_pinturas, name='planillaPinturasAdmin')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)