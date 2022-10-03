import flask, sqlite3
from flask import render_template, request



app = flask.Flask(__name__, template_folder="Task3_4_Marcus_1_1/templates")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/assessment", methods = ["POST"])
def synthesis():
    conn = sqlite3.connect("bakery.db")
    data = request.form['loc']
    print(data)
    curr = conn.execute("SELECT `Name`, `Type`, Price FROM Product WHERE `Location` = ? ORDER BY Price ASC", (str(data),))
    answers = list(curr)

    conn.close()

    return render_template("formresult.html", attr = answers)

if __name__ == "__main__":
    app.run()
    







