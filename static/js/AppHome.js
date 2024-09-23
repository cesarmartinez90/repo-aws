document.addEventListener('DOMContentLoaded', function() {

document.querySelector("#butt-reguser").addEventListener('click',reg_site);
document.querySelector("#butt-consultar").addEventListener('click',consultar_site);
});

function reg_site() {
    window.location = "/reg_view"
}

function consultar_site() {
    window.location = "/consultar_view"
}
