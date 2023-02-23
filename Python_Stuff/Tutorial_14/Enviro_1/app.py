import flask
from flask import url_for, render_template, redirect

app = flask.Flask(__name__)

@app.route("/")
def main():
    return redirect("/A/")

@app.route("/A/")
def A():
    return render_template("A.html")

@app.route("/B/")
def B():
    return render_template("B.html")

@app.route("/C/")
def C():
    return render_template("C.html")

@app.route("/D/")
def D():
    return render_template("D.html")

if __name__ == "__main__":
    app.run()