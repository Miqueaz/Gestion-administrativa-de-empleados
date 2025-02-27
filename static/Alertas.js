function Eliminar(ruta, id, password) {
  Swal.fire({
    title: "¿Estás seguro que deseas eliminarlo?",
    text: "No podrás revertirlo.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#f96332",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sí, Eliminar",
    cancelButtonText: "No, Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: "Ingresa la contraseña de administrador",
        input: "password",
        inputAttributes: {
          autocapitalize: "off",
        },
        showCancelButton: true,
        confirmButtonColor: "#f96332",
        confirmButtonText: "Sí, Confirmar",
        cancelButtonText: "No, Cancelar",
        showLoaderOnConfirm: true,
        preConfirm: async (password) => {
          try {
            const response = await fetch(`/OPPENHEIMER/verificar_contrasena/${password}/`, {
              method: 'GET',
              headers: {
                'Content-Type': 'application/json',
              },
            });

            if (!response.ok) {
              throw new Error('Contraseña incorrecta');
            }

            return true;
          } catch (error) {
            Swal.showValidationMessage(error.message);
          }
        },
        allowOutsideClick: () => !Swal.isLoading(),
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = `/OPPENHEIMER/${ruta}${id}/`;
        } else {
          Swal.fire({
            confirmButtonColor: "#f96332",
            icon: 'error',
            title: 'Cancelado',
            text: 'El objeto no se elimino.',
          });
        }
      });
    }
  });
}

document.getElementById('Guardar').addEventListener('click', function () {
  Swal.fire({
    title: "¿Quieres guardar los cambios?",
    showDenyButton: true,
    showCancelButton: true,
    confirmButtonColor: "#f96332",
    confirmButtonText: "Guardar",
    denyButtonText: `No guardar`
  }).then((result) => {
    if (result.isConfirmed) {
      document.getElementById('form').submit();
    } else if (result.isDenied) {
      Swal.fire("Cambios no guardados");
    }
  });
});


