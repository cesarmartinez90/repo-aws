from flask import Flask

app = Flask(__name__, template_folder="")

from routes.routes import *

if __name__ == "__main__":
    host = "172.31.33.130"
    port = "80"
    app.run(host,port, True)


