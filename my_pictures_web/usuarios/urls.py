from django.urls import path
from . import views

urlpatterns = [
    path('', views.main,name="main"),
    path('pintores/', views.pintores, name="pintores" ),
    path('pintores/detalles/<int:id>', views.detalles, name="detalles" ),
    path('crear-pintor', views.crear_pintor, name="crear_pintor" ),
    path('crear-pintura', views.crear_pintura, name="crear_pintura" ),
    path('detallePintura', views.detallePintura, name="detallePintura" ),
    path('planillaPinturasDina', views.planillaPinturas, name="planillaPinturasDina" )
]