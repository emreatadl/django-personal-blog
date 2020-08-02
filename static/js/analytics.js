(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-MZSS5HV');


function clickMenuItem1() {
    window.dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Menü",
     "eventLabel": "Hakkımda"
    });
}

function clickMenuItem2() {
    window.dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Menü",
     "eventLabel": "Blog"
    });
}

function clickAboutMe() {
    window.dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Header",
     "eventLabel": "Hakkımda"
    });
}

function clickLinkEdin() {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Sosyal Medya",
     "eventLabel": "Linkedin"
    });
}

async function clickInstagram() {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Sosyal Medya",
     "eventLabel": "Instagram"
    });
}

function clickGithub() {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Sosyal Medya",
     "eventLabel": "Github"
    });
}

function clickTwitter() {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
     "event": "GAEvent",
     "eventCategory": window.location.pathname,
     "eventAction": "Sosyal Medya",
     "eventLabel": "Twitter"
    });
}