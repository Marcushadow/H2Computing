import flask, sqlite3
from flask import render_template, request

app = flask.Flask(__name__, template_folder="TASK4_4_Marcus_1_1/templates")


@app.route("/")
def mainCode():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def synthesis():
    location = request.form['Location']
    conn = sqlite3.connect("equipment.db")

    curr = conn.execute("SELECT SerialNumber, Type FROM Device WHERE Location = ?", (location,))

    value = list(curr)

    conn.close()
    return render_template("display.html", attr = value)


if __name__ == "__main__":
    app.run()