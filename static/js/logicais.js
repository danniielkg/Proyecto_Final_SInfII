document.querySelector('#btnIngresar').addEventListener('click', iniciarSesion);

function iniciarSesion() {
    var sCorreo = '';
    var sContrasenna = '';
    var bAcceso = false;

    sCorreo = document.querySelector('#txtCorreo').value;
    sContrasenna = document.querySelector('#txtContrasenna').value;

    bAcceso = validarCredenciales(sCorreo,sContrasenna);
    console.log(bAcceso);

    if (bAcceso == true) {
        ingresar();
    }
}

function ingresar() {
    var rol = sessionStorage.getItem('rolUsuarioActivo');
    switch (rol) {
        case '1':
            window.location.href = 'http://localhost:3000/inicio';
        break;
        case '2':
            window.location.href = 'http://localhost:3000/carrito_compras';
        break; 
        case '3':
            window.location.href = 'http://localhost:3000/404';
        break; 
    }
}