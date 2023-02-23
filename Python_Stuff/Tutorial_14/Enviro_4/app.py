import flask
from flask import url_for, render_template, redirect

app = flask.Flask(__name__)

@app.route("/")
def main():
    return redirect("/Main/")

@app.route("/<s>/")
def A(s):
    s = s + "<h1>Hello this is an attempted injection</h1>"
    return render_template("secondaryRender.html", attribute = s)

if __name__ == "__main__":
    app.run()