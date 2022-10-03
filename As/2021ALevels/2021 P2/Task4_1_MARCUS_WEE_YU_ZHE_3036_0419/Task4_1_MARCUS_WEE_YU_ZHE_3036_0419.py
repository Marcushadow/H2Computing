import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route("/")
def main():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run()
