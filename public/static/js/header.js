
    // Funcionalidad de alternar entre modo oscuro y claro
    const toggleButton = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const darkModeEnabled = window.matchMedia('(prefers-color-scheme: dark)').matches || localStorage.getItem('theme') === 'dark';

    function setTheme(isDark) {
        if (isDark) {
            document.documentElement.classList.add('dark');
            themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m6.364 1.364l-.707.707M21 12h-1m-1.657-4.95l-.707-.707M4.636 4.636l.707.707M3 12h1m1.657 4.95l.707.707M19.364 19.364l-.707-.707M12 21v-1m-6.364-1.364l.707-.707"></path>';
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 118.646 3.646a9.003 9.003 0 0011.708 11.708z"></path>';
            localStorage.setItem('theme', 'light');
        }
    }

    toggleButton.addEventListener('click', () => {
        const isDark = !document.documentElement.classList.contains('dark');
        setTheme(isDark);
    });

    // Inicializa el tema según la preferencia del usuario
    setTheme(darkModeEnabled);

    // Funcionalidad del dropdown del perfil
    const profileButton = document.getElementById('profile-button');
    const profileMenu = document.getElementById('profile-menu');

    profileButton.addEventListener('click', (e) => {
        e.stopPropagation();
        profileMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', () => {
        profileMenu.classList.add('hidden');
    });

    profileMenu.addEventListener('click', (e) => {
        e.stopPropagation(); // Evitar que el dropdown se cierre si se hace clic dentro de él
    });
