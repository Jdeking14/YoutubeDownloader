$(document).ready(function(){
    $('#downloadForm').submit(function(e){
        e.preventDefault(); // Evita la recarga de la página
        $.ajax({
            url: '/descargar',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert("¡Descarga completada!");
            },
            error: function(xhr, status, error) {
                alert("Ocurrió un error al intentar descargar el video.");
            }
        });
    });
});
