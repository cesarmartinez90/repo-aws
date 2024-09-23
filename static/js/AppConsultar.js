function consultar_user(){
    id = document.getElementById('idUsr').value
    fetch('/consultar_user',{
        "method":"post",
        "headers":{"Content-type":"application/json"},
        "body": JSON.stringify(id)
    })
}