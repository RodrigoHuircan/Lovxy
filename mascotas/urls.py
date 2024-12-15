from django.urls import path
from .views import *

urlpatterns=[ 
    path('', Inicio, name = "Inicio"),
    path('Tienda/', Tienda, name = "Tienda"),
    path('Nosotros/', Nosotros, name = "Nosotros"),
    path('Galeria/', Galeria, name = "Galeria"),
    path('Contacto/', Contacto, name = "Contacto"),
    path('Registrar/', Registrar, name = "Registrar"),
    path('API/', API, name = "API"),
    path('CrearArt/', CrearArt, name = "CrearArt"),
    path('Disponible/', Disponible, name = "Disponible"),
    path('Eliminar/<id>', Eliminar, name = "Eliminar"),
    path('Modificar/<id>', Modificar, name = "Modificar"),
    path('Mostrar/', Mostrar, name = "Mostrar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
] 