from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    import bjoern

    bjoern.run(app, "127.0.0.1", 5000)
