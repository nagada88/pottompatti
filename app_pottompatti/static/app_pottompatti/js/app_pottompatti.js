let lastScrollTop = 0;
const navbar = document.getElementById("mynav");
const topbar = document.getElementById("topbar");
const navbarCollapse = document.getElementById("navbarNav");
const navbarToggler = document.querySelector(".navbar-toggler");

function isNavbarOpen() {
    return navbarCollapse.classList.contains("show") || document.body.classList.contains("menu-open");
  }
  
  navbarCollapse.addEventListener('shown.bs.collapse', () => {
    document.body.classList.add('menu-open');
    navbar.classList.remove('navbar-hidden'); // biztosan jelenjen meg
    topbar.classList.remove('topbar-hidden');
  });
  
  navbarCollapse.addEventListener('hidden.bs.collapse', () => {
    document.body.classList.remove('menu-open');
  });

// toggle body class menü nyitáskor
navbarToggler.addEventListener("click", () => {
  setTimeout(() => {
    if (navbarCollapse.classList.contains("show")) {
      document.body.classList.add("menu-open");
    } else {
      document.body.classList.remove("menu-open");
    }
  }, 350); // Bootstrap collapse animáció ideje
});

document.addEventListener('scroll', function() {
    document.querySelectorAll('.fade-in').forEach(function(el){
        const rect = el.getBoundingClientRect();
        if(rect.top < window.innerHeight - 150) {
            el.classList.add('visible');
        }
    });
    });
    document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function(){
        document.querySelectorAll('.fade-in-on-load').forEach(function(el){
            el.classList.add('visible');
            triggerFadeIn();
        });
    }, 500); // <-- 1000 ms = 1 másodperc késleltetés
    });
    
document.addEventListener("scroll", function () {
    if (document.body.classList.contains('menu-open')) return;
  
    const st = window.pageYOffset || document.documentElement.scrollTop;
  
    if (st > lastScrollTop && st > 80) {
      navbar.classList.add("navbar-hidden");
      topbar.classList.add("topbar-hidden");
    } else if (st < lastScrollTop) {
      navbar.classList.remove("navbar-hidden");
      if (st <= 50) {
        topbar.classList.remove("topbar-hidden");
      }
    }
  
    if (st <= 50) {
      navbar.classList.remove("scrolled");
    } else {
      navbar.classList.add("scrolled");
    }
  
    lastScrollTop = st <= 0 ? 0 : st;
  });

document.addEventListener("DOMContentLoaded", function() {
setTimeout(function(){
    document.querySelectorAll('.fade-in-on-load').forEach(function(el){
        el.classList.add('visible');
        triggerFadeIn();
    });
}, 500); // <-- 1000 ms = 1 másodperc késleltetés
});


function triggerFadeIn() {
document.querySelectorAll('.fade-in-htmx').forEach(function(el, index) {
    // Reset, ne legyen visible alapból
    el.classList.remove('visible');
    el.style.transitionDelay = (index * 100) + "ms"; 
});

// Kicsi várakozás, hogy az új DOM beépüljön
setTimeout(() => {
    document.querySelectorAll('.fade-in-htmx').forEach(function(el) {
        el.classList.add('visible');
    });
}, 150); // 150ms biztosan elég
}

document.body.addEventListener('htmx:afterSwap', function(e)
  {
    triggerFadeIn();
  }
);

document.body.addEventListener('htmx:afterSwap', function(e) {
  triggerFadeIn();

  e.target.querySelectorAll('[data-bs-toggle="modal"]').forEach(el => {
    el.addEventListener('click', function () {
      const target = el.getAttribute('data-bs-target');
      const modalEl = document.querySelector(target);
      if (modalEl) {
        const modal = new bootstrap.Modal(modalEl);
        modal.show();
      }
    });
  });
});


