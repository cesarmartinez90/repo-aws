from flask import Flask, render_template, request
from server import app
from database.db import *

@app.route('/reg_view')
def reg_view():
    return render_template('Register.html')

@app.route('/consultar_view')
def consultar_view():
    return render_template('Consultar.html')


@app.route('/reg_user', methods=["post"])
def reg_user():
    data = request.form
    id = data["id"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    actividad = data["actividad"]
    estado = data["estado"]
    cargo = data["cargo"]
    fecha = data["fecha"]
    insert(id, nombre, apellido, actividad, estado, cargo, fecha)
    return "Usuario Agregado"

@app.route('/consultar_user', methods=["post"])
def consultar_user():
    id = request.get_json()
    result= consulta(id)
    print(result)
    return "Usuario Consultado"
  

#@app.route('/consulta_user')
#def consulta_user():
 #   result= consulta('202')
 # #  print(result)
   # return "Usuario Consultado"