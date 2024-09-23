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
       document.getElementById("img_response").src = "https://bucket-aws15-curso.s3.us-east-2.amazonaws.com/images/" + data.photo
    })

} 