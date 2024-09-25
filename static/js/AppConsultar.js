function consultar_user(){
    id = document.getElementById('idUsr').value
    fetch('/consultar_user',{
        "method":"post",
        "headers":{"Content-type":"application/json"},
        "body": JSON.stringify(id)
        
    })
    .then(resp => resp.json())
    .then(data => {
        document.getElementById("txt_response").value = data.nombre + " " + data.apellido + " " + data.actividad + " " + data.fecha
            // Photo
        const userImage = document.getElementById("user_image");
        userImage.src = data.photo;  // Usa la URL devuelta por el servidor
        userImage.style.display = "block";  // Asegúrate de que la imagen se muestre
            // URL
        const imageLink = document.getElementById("image_link");
        imageLink.innerHTML = `<a href="${data.photo}" target="_blank">Ver Imagen</a>`;
    
    })

} 