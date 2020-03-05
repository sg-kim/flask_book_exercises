from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello Flask!</h1>"

if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
