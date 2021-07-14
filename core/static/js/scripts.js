function eliminarTema() {
    var idTema = $("#txtIDTema").val();
    swal({
        title: "¿Eliminar Tema?",
        text: "Los datos se eliminan en cascada, se eliminarán todos los registros asociados al tema",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_tema",
                data: {
                    idTema: idTema,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        window.location.href = "/temas"
                    }
                }
            });
        }
    });
    return false;
}

function eliminarCapa() {
    var idCapa = $("#txtIDCapacitacion").val();
    swal({
        title: "¿Eliminar Capacitación?",
        text: "Los datos se eliminan en cascada, se eliminarán todos los registros asociados a la capacitación",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_capa",
                data: {
                    idCapa: idCapa,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        window.location.href = "/capacitaciones"
                    }
                }
            });
        }
    });
    return false;
}

function eliminarArchivo(e) {
    var elemento = e;
    swal({
        title: "¿Eliminar Archivo Adjunto?",
        text: "El Archivo adjunto a este tema será eliminado.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_adjunto",
                data: {
                    idArchivo: elemento.id,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.reload();
                    }
                }
            });
        }
    });
}

function eliminarInvitado(e) {
    var elemento = e;
    swal({
        title: "¿Eliminar Invitado?",
        text: "La información asocidada se elimina en cascada.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_invitado",
                data: {
                    idInvitado: elemento.id,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.reload();
                    }
                }
            });
        }
    });
}

function eliminarAsitente(e) {
    swal({
        title: "¿Eliminar Asistente?",
        text: "La información asocidada se elimina en cascada.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_asistente",
                data: {
                    idAsistencia: e.id,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.reload();
                    }
                }
            });
        }
    });
}

function eliminarHito(e) {
    var idCapa = $("#idCapa").val();
    var idHito = $("#idHito").val();
    swal({
        title: "¿Eliminar Hito?",
        text: "La información asocidada se elimina en cascada.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_hito",
                data: {
                    idHito: idHito,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.href = "../../invitadoshitos/" + idCapa;
                    }
                }
            });
        }
    });
}

function cerrarHito() {
    var idCapa = $("#idCapa").val();
    var idHito = $("#idHito").val();
    swal({
        title: "¿Cerrar Hito?",
        text: "La Actualización de estado solo es para la estadística (por ahora).",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Cerrar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "cerrar_hito",
                data: {
                    idHito: idHito,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.href = "../../invitadoshitos/" + idCapa;
                    }
                }
            });
        }
    });
}


function eliminarArchivoCapacitacion(e) {
    var elemento = e;
    swal({
        title: "¿Eliminar Archivo Adjunto?",
        text: "El Archivo adjunto a este tema será eliminado.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_adjunto_capa",
                data: {
                    idArchivo: elemento.id,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.reload();
                    }
                }
            });
        }
    });
}

function eliminarAdjuntoHito(e) {
    var elemento = e;
    swal({
        title: "¿Eliminar Archivo Adjunto?",
        text: "El Archivo adjunto a este tema será eliminado.",
        icon: "warning",
        buttons: {
            confirm: {
                text: "Eliminar",
                value: true,
                visible: true,
                closeModal: true
            },
            cancel: {
                text: "Cancelar",
                value: false,
                visible: true,
                closeModal: true
            }
        },
        dangerMode: true,
        reverseButtons: true
    }).then((value) => {
        if (value) {
            $.ajax({
                type: "POST",
                url: "eliminar_adjunto_hito",
                data: {
                    idArchivo: elemento.id,
                },
                success: function (resultado) {
                    if (resultado === "OK") {
                        location.reload();
                    }
                }
            });
        }
    });
}

function validarForm() {
    var gerencia = $("#cmbGerencia").val();
    if (gerencia) {
        return true;
    } else {
        errorMessage('Error procesaro formulario', 'Seleccionar Gerencia');
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