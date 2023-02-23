import flask
from flask import url_for, render_template, redirect

app = flask.Flask(__name__)

@app.route("/")
def main():
    return redirect("/Main/")

@app.route("/<s>/")
def A(s):
    return render_template("mainRender.html", attribute = s)

if __name__ == "__main__":
    app.run()