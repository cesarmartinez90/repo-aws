from flask import Flask, render_template, request, jsonify
from server import app
from database.db import *
from control.adminS3 import *

@app.route('/')
def home_view():
    return render_template('home.html')

@app.route('/reg_view')
def reg_view():
    return render_template('Register.html')

@app.route('/consultar_view')
def consultar_view():
    return render_template('Consultar.html')


@app.route('/reg_user', methods=["post"])
def reg_user():
    data = request.form
    file = request.files 
    id = data["id"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    actividad = data["actividad"]
    estado = data["estado"]
    cargo = data["cargo"]
    fecha = data["fecha"]
    photo = file["photo"]
    photo_path, photo_name = save_photo(id, photo)
    sessionS3 = connectionS3()
    upload_photoS3(sessionS3, photo_path, photo_name)
    insert(id, nombre, apellido, actividad, estado, cargo, fecha)

    return "Usuario Agregado"

@app.route('/consultar_user', methods=["post"])
def consultar_user():
    id = request.get_json()
    result= consulta(id)
    file_found = get_file()
    resp_data = {
        'nombre': result[0][1],
        'apellido': result[0][2],
        'actividad': result[0][3],
        'fecha': result[0][6],
        'photo': file_found
    }
    return jsonify(resp_data)
    print(result)
    return "Usuario Consultado"
  

#@app.route('/consulta_user')
#def consulta_user():
 #   result= consulta('202')
 # #  print(result)
   # return "Usuario Consultado"