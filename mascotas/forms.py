#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo', 'nombre', 'precio', 'categoria','tipo', 'tamaño', 'cantidad' , 'imagen']
        labels = {
            'codigo' : "Codigo",
            'nombre' : "Nombre",
            'precio' : "Precio",
            'categoria' : "Categoria",
            'tipo' : "Tipo",
            'tamaño' : "Tamaño",
            'cantidad' : 'Cantidad',
            'imagen': "Imagen",
        }
        widgets={
            'codigo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el codigo',
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el nombre',
                    'class' : 'form-control',
                    'id' : 'nombre'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el precio',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'categoria'
                }
            ),
            'tipo':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el tipo',
                    'class' : 'form-control',
                    'id' : 'tipo'
                }
            ),
            'tamaño':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el tamaño',
                    'class' : 'form-control',
                    'id' : 'tamaño'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese la cantidad',
                    'class' : 'form-control',
                    'id' : 'cantidad'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            )
        }


class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']