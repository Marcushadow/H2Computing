import flask
from flask import redirect, url_for
app = flask.Flask(__name__)


@app.route("/redirectfor/")
def redirfor():
    return redirect(url_for("redirect"))

@app.route("/redirect/")
def redir():
    return redirect("https://www.youtube.com/watch?v=3PHhl2pa3jo")

@app.route("/textReturn/")
def text():
    headers = {"Content-Type": "text/plain"}
    return ("<p> Not html </p>", 200, headers)


if __name__ == "__main__":
    app.run()