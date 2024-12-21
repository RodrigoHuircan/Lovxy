function alertaNoAutenticado() {
    Swal.fire({
        icon: 'warning',
        title: 'Acción no permitida',
        text: 'Debes iniciar sesión para realizar compras.',
        confirmButtonText: 'Iniciar sesión',
        footer: `<a href="${inicioUrl}">Ir a la página de inicio de sesión</a>`,
        customClass: {
            confirmButton: 'btn-custom',
            footer: 'footer-custom', 
        },
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = loginUrl;
        }
    });
}


function handleFormSubmit(formId, loginUrl){
    document.addEventListener('DOMContentLoaded', function() {
        const registroForm = document.getElementById(formId);
    
        if (registroForm) {
            registroForm.addEventListener('submit', function(event){
                event.preventDefault();
                const form = this;
                const formData = new FormData(form);
    
                fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers:{
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if(data.success) {
                        Swal.fire({
                            icon: 'success',
                            title: '!Registro exitoso!',
                            text: data.message,
                            confirmButtonText: 'Ir a Login',
                            allowOutsideClick: false,
                            customClass: {
                                confirmButton: 'btn-custom',
                            },
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.location.href = loginUrl;
                            }
                        });
                    }
                    else{
                        const errors = JSON.parse(data.errors);
                        let errorMessage = "";
                        for (let field in errors){
                            errorMessage += errors[field].map(err => err.message).join('\n') + '\n';
                        }
                        Swal.fire({
                            icon: 'error',
                            title: 'Error en el registro',
                            text: errorMessage,
                        });
                    }
                })
                .catch(error => console.error('Error:', error));
            });
        }
    });
}


handleFormSubmit('registroForm', "{% url 'login' %}");


