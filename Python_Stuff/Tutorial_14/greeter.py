import flask

app = flask.Flask(__name__)

@app.route("/greet/<s>/")
def greet(s):
    return f"Hello, {s}"




if __name__ == "__main__":
    app.run()