let lastScrollTop = 0;

document.addEventListener("scroll", function() {
const st = window.pageYOffset || document.documentElement.scrollTop;
const navbar = document.getElementById("mynav");
const topbar = document.getElementById("topbar");

// TOPBAR és NAVBAR csak ha tényleg görgetsz le
if (st > lastScrollTop && st > 80) {  // csak ha lejjebb vagy mint 80px
    navbar.classList.add('navbar-hidden');
    topbar.classList.add('topbar-hidden');
} else if (st < lastScrollTop) {
    // felfelé görgetés
    navbar.classList.remove('navbar-hidden');
    if (st <= 50) {
        topbar.classList.remove('topbar-hidden');
    }
}

// átlátszó header effekthez
if (st <= 50) {
    navbar.classList.remove('scrolled');
} else {
    navbar.classList.add('scrolled');
}

lastScrollTop = st <= 0 ? 0 : st; // ne legyen negatív
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
