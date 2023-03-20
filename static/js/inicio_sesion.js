/*Roles: 1:Administrador
         2:Cliente
*/

function obtenerListaUsuarios() {
    var listaUsuarios = JSON.parse(localStorage.getItem('listaUsuariosLs'));

    if (listaUsuarios == null) {
        listaUsuarios = [
            ['1','Daniel','Chacon','admin@gmail.com','admin123','1994-12-12','1'],
            ['2','Paula','Rosero','cliente@gmail.com','cliente123','1995-12-15','2'],
            ['3','abc','abc','abc','123','2023-03-17','3']
        ]
    }
    return listaUsuarios;
}

function validarCredenciales(pCorreo,pContrasenna) {
    var listaUsuarios = obtenerListaUsuarios();
    var bAcceso = false;

    for (var i = 0; i < listaUsuarios.length; i++) {
        if (pCorreo == listaUsuarios[i][3] && pContrasenna == listaUsuarios[i][4]) {
            bAcceso = true;
            sessionStorage.setItem('usuarioActivo', listaUsuarios[i][1] + ' ' + listaUsuarios[i][2]);
            sessionStorage.setItem('rolUsuarioActivo', listaUsuarios[i][6]);
        }
    }
    return bAcceso;
}