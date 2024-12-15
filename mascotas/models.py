import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True, verbose_name = "Id de Categoria")
    nombreCategoria = models.CharField(max_length = 50, blank = True, verbose_name ="Nombre de Categoria")


    def __str__(self):
        return self.nombreCategoria #devuelve un string para acceder a los objetos almacenados

class Articulo(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 8, verbose_name = "ID")
    nombre = models.CharField(max_length = 50, blank = True, verbose_name = "Marca")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    tipo = models.CharField(max_length = 50, blank = True, verbose_name = "Tipo")
    tamaño = models.CharField(max_length = 8, blank = True, verbose_name = "Tamaño")
    imagen = models.ImageField(upload_to = "imagenes", null = True, blank = True, verbose_name = "Imagen")
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoria")
    cantidad = models.IntegerField(blank=True, null=True, verbose_name="Cantidad")

    def __str__(self):
        return self.codigo

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True, verbose_name = "ID")
    total = models.BigIntegerField(verbose_name = "Total")
    fechaCompra = models.DateTimeField(blank=False, null=False, default = datetime.datetime.now, verbose_name = "Fecha de Compra")
    usuario = models.CharField(max_length = 50, blank = True, verbose_name = "Usuario")
    estado = models.CharField(max_length = 50, blank = True, verbose_name = "Estado")
    impuesto = models.IntegerField(blank=True, null=True, verbose_name="Impuesto")
    envio = models.IntegerField(blank=True, null=True, verbose_name="Envio")
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    codigo = models.ForeignKey('Articulo', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
    
