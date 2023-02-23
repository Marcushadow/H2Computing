import flask, sqlite3
from flask import render_template, request


app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
