from django.shortcuts import render, redirect
from .models import Articulo, Boleta, detalle_boleta
from .forms import ArticuloForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from mascotas.compra import Carrito
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def Inicio(request):
    return render(request,'Inicio.html')

def Tienda(request):
    return render(request,'Tienda.html')

def Nosotros(request):
    return render(request,'Nosotros.html')

def Galeria(request):
    return render(request,'Galeria.html')

def Contacto(request):
    return render(request,'Contacto.html')

def API(request):
    return render(request,'API.html')



@login_required
def Disponible(request):
    articulos = Articulo.objects.raw('SELECT * FROM mascotas_articulo')
    print(articulos)
    datos = {'articulos' : articulos}
    return render(request, 'Disponible.html', datos)


@login_required
def CrearArt(request):
    if request.method == "POST":
        articuloform = ArticuloForm(request.POST,request.FILES) 
        if articuloform.is_valid():
            articuloform.save() 
            return redirect ('Disponible')
    else:
        articuloform=ArticuloForm()
    return render(request, 'CrearArt.html', {'articuloform' : ArticuloForm})


@login_required
def Eliminar(request, id):
    articuloEliminado=Articulo.objects.get(codigo=id) 
    articuloEliminado.delete()
    return redirect('Disponible')


@login_required
def Modificar(request, id):
    articuloModificado = Articulo.objects.get(codigo=id)
    datos ={
        'form': ArticuloForm(instance=articuloModificado) 
    }
    if request.method=="POST":
        formulario = ArticuloForm(data=request.POST, instance=articuloModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('Disponible')
    return render(request,'Modificar.html', datos)

def Registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            grupo_clientes = Group.objects.get(name='Clientes')
            usuario.groups.add(grupo_clientes)
            return JsonResponse({'success': True, 'message': 'Registro exitoso. Por favor, inicia sesión.'})
        else:
            return JsonResponse({'success': False, 'message': formulario.errors.as_json()})
 
    return render(request,'registration/Registrar.html', data)

def Mostrar(request):
    articulitos = Articulo.objects.all()
    datos = {
        'articulitos': articulitos
    }
    return render(request, 'Mostrar.html', datos)

def Tienda(request):
    articulitos = Articulo.objects.all()
    elementos_por_pagina = 6
    paginator = Paginator(articulitos, elementos_por_pagina)
    page = request.GET.get('page')
    articulitos_paginados = paginator.get_page(page)
    datos = {
        'articulitos': articulitos_paginados
    }
    return render(request, 'Tienda.html', datos)


def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.agregar(articulo = articulo)
    return redirect('Tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.eliminar(articulo=articulo)
    return redirect('Tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.restar(articulo=articulo)
    return redirect('Tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('Tienda')    


@login_required
def generarBoleta(request):
    precio_total=0
    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total, usuario = user)
    boleta.estado = "Procesando"
    boleta.impuesto = precio_total * 0.19
    boleta.envio = 5000
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Articulo.objects.get(codigo = value['codigo'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, codigo = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
            #producto.delete()
            if cant <= producto.cantidad:
                producto.cantidad -= cant
                producto.save()
            elif cant > producto.cantidad:
                mensaje = "No hay stock disponible"
                return render(request, 'Tienda.html', {'mensaje' : mensaje})
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'estado': boleta.estado,
        'usuario': boleta.usuario,
        'total': boleta.total,
        'envio': boleta.envio,
        'impuesto': boleta.impuesto
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()

    return render(request, 'Detallecarrito.html',datos)
  
   