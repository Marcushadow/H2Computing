import flask

from flask import url_for, render_template

app = flask.Flask(__name__)

@app.route("/")
def home():
    return render_template("links.html")

@app.route("/greeting")
def hello():
    return "Hello, World!"

@app.route("/<int:i>")
def report(i):
    return f"Year is {i}"



if __name__ == "__main__":
    app.run()