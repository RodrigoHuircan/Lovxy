//validar

$(function(){
    $("#LovxyForm").validate({
        rules:{
            nom:{
                required: true},
            apeP:{
                required: true},
            apeM:{
                required: true},
            correo:{
                required:true,
                email: true},
            fono:{
                required: true},
            contacto:{
                required: true}
        }, //?reglas del formulario

        messages:{
            nom:{
                required: 'Ingrese nombre de usuario',
                minlength: 'Carácteres insuficientes (mínimo 3)'
            },
            apeP:{
                required: 'Ingrese apellido paterno de usuario',
                minlength: 'Carácteres insuficientes (mínimo 3)'
            },
            apeM:{
                required: 'Ingrese apellido materno de usuario',
                minlength: 'Carácteres insuficientes (mínimo 3)'
            },
            correo:{
                required: 'Ingrese un correo electrónico',
                email: 'Formato de correo no válido'
            },
            fono:{
                required: 'Ingrese un número de teléfono',
                minlength: 'Cantidad de carácteres insuficientes'
            },
            contacto:{
                required: 'Es necesario tickear la casilla del formulario'
            }
        },
    })
})

//dom

function upperText(texto)
  {
      const x = texto;
      x.value= x.value.toUpperCase();
  }
