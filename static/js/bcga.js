document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu_toggle");
    const sidebar = document.getElementById("sidebar");
    const close = document.getElementById("close");

    menuToggle.addEventListener("click", function () {
        sidebar.classList.toggle("-translate-x-full");
    });
    close.addEventListener("click", function () {
        sidebar.classList.toggle("-translate-x-full");
    });
});

const carousel = document.querySelector('.carousel');
const slides = document.querySelectorAll('.carousel-slide');
const prevButton = document.querySelector('#prevButton');
const nextButton = document.querySelector('#nextButton');
let currentSlide = 0;

function goToSlide(slideIndex) {
    slides.forEach((slide, index) => {
        slide.classList.toggle(`-translate-x-full`);
        console.log(slideIndex)
    });
    currentSlide = slideIndex;
}

prevButton.addEventListener('click', () => {
    if (currentSlide > 0) {
        goToSlide(currentSlide - 1);
    }
});

nextButton.addEventListener('click', () => {
    if (currentSlide < slides.length - 1) {
        goToSlide(currentSlide + 1);
    }
});

