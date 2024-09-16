from flask import Flask, render_template

app = Flask(__name__, template_folder="")

@app.route('/')
def home():
    return render_template('Register.html')


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4000
    app.run(host,port, True)