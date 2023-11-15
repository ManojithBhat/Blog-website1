const menuToggleIcon = document.querySelector(".menu-toggle-icon");
const menuIcon = document.querySelectorAll('.menu-icon');
const search = document.querySelector('.form-nav-bar')

const toggleMenu = () => {
    const hambMenu = document.querySelector('.menu');
    if (hambMenu.style.opacity == 1) {
        hambMenu.style.opacity = 0;
        menuIcon[0].style.display = "block";
        menuIcon[1].style.display = "none";

    }
    else {
        hambMenu.style.opacity = 1;
        menuIcon[0].style.display = "none";
        menuIcon[1].style.display = "block";
        search.style.display = "none";
    }

}

menuToggleIcon.addEventListener('click', toggleMenu)