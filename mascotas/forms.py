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
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirma la contraseña',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, números y @/./+/-/_',
            'password1': 'Debe contener al menos 8 caracteres.',
            'password2': 'Introduce la misma contraseña para verificar.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sobrescribir etiquetas de los campos
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirma tu contraseña'

        # Personalizar textos de ayuda
        self.fields['password1'].help_text = (
            'Tu contraseña debe contener al menos 8 caracteres, '
            'no puede ser una contraseña común y no debe estar compuesta solo de números.'
        )
        self.fields['password2'].help_text = 'Por favor, repite la misma contraseña para confirmarla.'

        # Opcional: Personalizamos los mensajes de error
        self.fields['password1'].error_messages = {
            'required': 'Este campo es obligatorio.',
        }
        self.fields['password2'].error_messages = {
            'required': 'Este campo es obligatorio.',
        }