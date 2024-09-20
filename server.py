from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__, template_folder="")

@app.route('/reg_view')
def reg_view():
    return render_template('Register.html')


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

if __name__ == "__main__":
    host = "172.31.33.130"
    port = "80"
    app.run(host,port, True)