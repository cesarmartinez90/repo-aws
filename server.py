from flask import Flask, render_template
from database.db import *

app = Flask(__name__, template_folder="")

@app.route('/reg_view')
def reg_view():
    return render_template('Register.html')


@app.route('/reg_user')
def reg_user():
    insert()
    return "Usuario Agregado"

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4000
    app.run(host,port, True)