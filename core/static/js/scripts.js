$(document).ready()

function test() {
    $.ajax({
        type: "POST",
        url: "ajaxtest",
        data: {
            user: 'teXDst'
        },
        success: function (resultado) {
            console.log(resultado);
        }
    })
}

function validarForm() {
    var archivo = $("#flsArchivos")[0].files;
    if (archivo.length > 0) {
        return true;
    } else {
        errorMessage('Seleccionar Archivo(s).', 'Se debe seleccionar por lo menos 1 archivo.')
        return false;
    }
}

function manejarrespuesta(respuesta) {
    errorMessage('xd', respuesta);
}

function errorMessage(titulo, mensaje) {
    swal({
        title: titulo,
        text: mensaje,
        icon: "error",
        button: true
    });
}