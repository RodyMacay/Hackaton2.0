document.addEventListener('DOMContentLoaded', function () {
    // Seleccionar el input de archivos y el contenedor de previsualización usando los IDs que se pasan en el HTML
    const fileUpload = document.getElementById('file-upload');
    const imagePreviewContainer = document.getElementById('image-preview');

    if (fileUpload && imagePreviewContainer) {
        fileUpload.addEventListener('change', function (event) {
            const files = event.target.files;

            // Limpiar las imágenes anteriores
            imagePreviewContainer.innerHTML = '';

            if (files && files.length > 0) {
                Array.from(files).forEach(file => {
                    if (file.type.startsWith('image/')) {
                        const reader = new FileReader();

                        reader.onload = function (e) {
                            // Crear un elemento de imagen para cada archivo
                            const img = document.createElement('img');
                            img.src = e.target.result;
                            img.classList.add('h-32', 'w-32', 'object-cover', 'rounded-md', 'border');
                            imagePreviewContainer.appendChild(img);
                        };

                        reader.readAsDataURL(file);
                    } else {
                        // Mostrar mensaje de error si el archivo no es una imagen
                        const feedback = document.getElementById('upload-feedback');
                        if (feedback) {
                            feedback.textContent = "Formato de archivo no permitido.";
                            feedback.classList.remove('hidden');
                        }
                    }
                });

                // Mostrar el contenedor si hay imágenes
                imagePreviewContainer.classList.remove('hidden');
            } else {
                // Ocultar el contenedor si no hay imágenes seleccionadas
                imagePreviewContainer.classList.add('hidden');
            }
        });
    }
});
