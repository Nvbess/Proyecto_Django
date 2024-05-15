function confirmarEliminar(id) {
    Swal.fire({
        title: "Esta seguro de querer eliminar?",
        text: "Esta acción no se puede deshacer",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
        // desde acá se inicia la confirmación a la cual le agregamos la combinacion con el sistema //
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Eliminada!",
                text: "La obra ha sido eliminada",
                icon: "success"
                // Creamos un then luego del boton de confirmación para ejecutar la acción en la BD //
            }).then(function () {
                window.location.href = "delete/" + id + "/";
            });
        }
    });
}

function messages(){
    const Toast = Swal.mixin({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 6000,
        timerProgressBar: true,
        didOpen: (toast) => {
        toast.onmouseenter = Swal.stopTimer;
        toast.onmouseleave = Swal.resumeTimer;
        }
    });
    Toast.fire({
        icon: "success",
        title: "Registro Completado Exitosamente!"
    });
}
