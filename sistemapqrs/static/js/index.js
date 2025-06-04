function oficinaagregar() {
  document.addEventListener("DOMContentLoaded", function () {
    const formularioOficina = document.getElementById("form-oficina");
    if (formularioOficina) {
      formularioOficina.addEventListener("submit", function () {
        alert("Oficina agregado con éxito!");
      });
    }
  });
}
oficinaagregar();

function empleadoagregar() {
  document.addEventListener("DOMContentLoaded", function () {
    const formularioEmpleado = document.getElementById("form-empleado");
    if (formularioEmpleado) {
      formularioEmpleado.addEventListener("submit", function () {
        alert("Empleado agregado con éxito!");
      });
    }
  });
}
empleadoagregar();

function solicitudagregar() {
  document.addEventListener("DOMContentLoaded", function () {
    const formularioSolicitud = document.getElementById("form-solicitud");
    if (formularioSolicitud) {
      formularioSolicitud.addEventListener("submit", function () {
        alert("Solicitud agregado con éxito!");
      });
    }
    else{
      console.error("Formulario de solicitud no encontrado");
    }
  });
}
solicitudagregar();

function BarriosApi() {
  document.addEventListener("DOMContentLoaded", async function () {
    const campoBarrio = document.getElementById("campo-barrio");
    try {
      const respuesta = await fetch("/static/apibarrios.json");
      const datos = await respuesta.json();
      if (campoBarrio) {
        campoBarrio.innerHTML =
          '<option value="">Seleccione un barrio</option>';
        const barriosUnicos = [...new Set(datos.map((item) => item.Barrio))];
        barriosUnicos.forEach((barrio) => {
          const opcion = document.createElement("option");
          opcion.value = barrio;
          opcion.textContent = barrio;
          campoBarrio.appendChild(opcion);
        });
      }
    } catch (error) {
      campoBarrio.innerHTML =
        '<option value="">Error al cargar barrios</option>';
      console.error("Error cargando barrios:", error);
    }
  });
}
BarriosApi();


function GuardarDatosSeleccionados(){
document.addEventListener("DOMContentLoaded", function () {
const tipoSelect = document.getElementById("id_solForma");
const camposIdentidad = document.getElementById("selecciones");
  function actualizarFormulario() {
    const valor = tipoSelect.value;

    if (valor === "Anonimo") {
      camposIdentidad.style.display = "none";
      const nombre = document.getElementById("id_solNombreCiudadano");
      const correo = document.getElementById("id_solCorreoElectronico");

      if (nombre) nombre.value = "";
      if (correo) correo.value = "";
    } else {
      camposIdentidad.style.display = "block";
    }
  }

  if (tipoSelect) {
    tipoSelect.addEventListener("change", actualizarFormulario);
    actualizarFormulario();
  } else {
    console.error("No se encontró el campo 'solForma'");
  }
});
}
GuardarDatosSeleccionados();
