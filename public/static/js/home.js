document.addEventListener('DOMContentLoaded', function() {
    let nextPageUrl = null;
    let prevPageUrl = null;
    let nextPageUrlAlbums = null;
    let prevPageUrlAlbums = null;

    function loadPhotos(url = '/photos/api/recent/') {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const recentPhotosContainer = document.querySelector('#recent-photos');
                const noPhotosMessage = document.getElementById('no-photos-message');
                const photoPagination = document.getElementById('photo-pagination');
                
                recentPhotosContainer.innerHTML = '';
                
                if (data.results.length > 0) {
                    noPhotosMessage.style.display = 'none';
                    photoPagination.style.display = 'flex';

                    data.results.forEach(photo => {
                        const createdAt = new Date(photo.created_at);
                        const formattedDate = `${createdAt.toLocaleDateString('es-ES', {
                            month: 'long', 
                            day: 'numeric', 
                            year: 'numeric'
                        })} ${createdAt.toLocaleTimeString('es-ES', {
                            hour: '2-digit', 
                            minute: '2-digit'
                        })}`;
                    
                        const photoElement = document.createElement('div');
                        photoElement.className = 'relative group';
                        photoElement.innerHTML = `
                            <img src="${photo.image}" alt="Foto en ${photo.album_name}" class="rounded-lg shadow-md object-cover h-48 w-full">
                            <div class="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 flex items-center justify-center rounded-lg transition-opacity">
                                <p class="text-white text-sm">${formattedDate || 'Sin descripción'}</p>
                            </div>
                        `;
                        recentPhotosContainer.appendChild(photoElement);
                    });
                } else {
                    noPhotosMessage.style.display = 'block';
                    photoPagination.style.display = 'none';
                }

                nextPageUrl = data.next;
                prevPageUrl = data.previous;

                const nextPageButton = document.querySelector('#next-page-button');
                const prevPageButton = document.querySelector('#prev-page-button');

                if (nextPageButton) nextPageButton.disabled = !nextPageUrl;
                if (prevPageButton) prevPageButton.disabled = !prevPageUrl;
            })
            .catch(error => console.error('Error al cargar las fotos recientes:', error));
    }

    function loadAlbums(url = '/albums/api/') {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const albumsContainer = document.querySelector('#albums');
                const noAlbumsMessage = document.getElementById('no-albums-message');
                const albumPagination = document.getElementById('album-pagination');
                
                albumsContainer.innerHTML = '';
                
                if (data.results.length > 0) {
                    noAlbumsMessage.style.display = 'none';
                    albumPagination.style.display = 'flex';

                    data.results.forEach(album => {
                        const albumElement = document.createElement('div');
                        albumElement.className = 'bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-hidden transform transition duration-300 hover:scale-105';
                        
                        const lastPhotoUrl = album.last_photo ? album.last_photo.image_url : 'placeholder_image_url.jpg';

                        albumElement.innerHTML = `
                            <div class="absolute top-2 right-2 bg-yellow-500 text-gray-900 text-xs font-bold px-2 py-1 rounded-full shadow">
                                ${album.photo_count || 0} Fotos
                            </div>
                            <img src="${lastPhotoUrl}" alt="Última foto en el álbum ${album.name}" class="w-full h-48 object-cover transition-opacity duration-200 hover:opacity-90">
                            <div class="p-4">
                                <h3 class="text-lg font-medium text-gray-900 dark:text-white">${album.name}</h3>
                                <p class="text-gray-500 dark:text-gray-400">Última actualización: ${album.updated_at || 'Sin fecha'}</p>
                                <p class="text-gray-600 dark:text-gray-400 mb-3">${album.description || 'Sin descripción'}</p>
                                <a href="/albums/${album.id}/" class="inline-block bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-medium py-1 px-3 rounded-full shadow-md transition-all duration-300 transform hover:-translate-y-1">
                                    Ver Álbum
                                </a>
                            </div>
                        `;
                        albumsContainer.appendChild(albumElement);
                    });
                } else {
                    noAlbumsMessage.style.display = 'block';
                    albumPagination.style.display = 'none';
                }

                nextPageUrlAlbums = data.next;
                prevPageUrlAlbums = data.previous;

                const albumNextPageButton = document.querySelector('#album-next-page-button');
                const albumPrevPageButton = document.querySelector('#album-prev-page-button');

                if (albumNextPageButton) albumNextPageButton.disabled = !nextPageUrlAlbums;
                if (albumPrevPageButton) albumPrevPageButton.disabled = !prevPageUrlAlbums;
            })
            .catch(error => console.error('Error al cargar los álbumes:', error));
    }

    loadPhotos();
    loadAlbums();
});
