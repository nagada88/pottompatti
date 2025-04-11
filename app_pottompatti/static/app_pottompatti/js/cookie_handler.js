document.addEventListener("DOMContentLoaded", function () {
    console.log("🚀 JavaScript betöltődött!");

    const cookieGroup = "analytics";
    const cookieValue = getCookie(cookieGroup);

    if (cookieValue === "accepted") {
        console.log("✅ Süti elfogadva, script betöltése...");
        loadAnalytics();
        hideBanner();
    } else if (cookieValue === "declined") {
        console.log("🚫 Süti elutasítva, script nem tölt be.");
        hideBanner();
    } else {
        console.log("⚠️ Süti státusz ismeretlen, banner megjelenik!");
        showBanner();
    }

    document.querySelectorAll(".cc-cookie-accept").forEach(button => {
        button.addEventListener("click", () => {
            console.log("✅ Elfogadva");
            setCookie(cookieGroup, "accepted", 365);
            loadAnalytics();
            hideBanner();
        });
    });

    document.querySelectorAll(".cc-cookie-decline").forEach(button => {
        button.addEventListener("click", () => {
            console.log("🚫 Elutasítva");
            setCookie(cookieGroup, "declined", 365);
            hideBanner();
        });
    });
});

// 🧠 Segédfüggvények

function setCookie(name, value, days) {
    const d = new Date();
    d.setTime(d.getTime() + (days*24*60*60*1000));
    const expires = "expires="+ d.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let c of cookies) {
        while (c.charAt(0) === ' ') c = c.substring(1);
        if (c.indexOf(name + "=") === 0) return c.substring((name + "=").length, c.length);
    }
    return null;
}

function loadAnalytics() {
    // Ide írd be a scriptet, amit el szeretnél indítani ha elfogadta:
    let script = document.createElement("script");
    script.src = "https://www.googletagmanager.com/gtag/js?id=G-WV9S75XT3C";
    script.async = true;
    document.head.appendChild(script);

    script.onload = () => {
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-WV9S75XT3C');
        console.log("📊 Google Analytics inicializálva.");
    };
}

function hideBanner() {
    document.getElementById("cookie-banner").style.display = "none";
}

function showBanner() {
    document.getElementById("cookie-banner").style.display = "flex";
}
