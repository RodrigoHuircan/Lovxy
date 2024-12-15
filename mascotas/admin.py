from django.contrib import admin
from .models import Categoria, Articulo, Boleta, detalle_boleta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)