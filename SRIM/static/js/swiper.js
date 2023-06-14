let swiper = new Swiper('.mySwiper', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  loop: true,
  autoplay: {
    delay: 6000,
  },
  speed: 1300,
});

let buttons = document.querySelectorAll('.scroll-down');
let target = document.querySelector('.title');

buttons.forEach((button) => {
  button.addEventListener('click', function () {
    target.scrollIntoView({ behavior: 'smooth' });
  });
});
