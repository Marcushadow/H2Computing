import flask, sqlite3

from flask import render_template, request

app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/latecomers")
def latecome():
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT Person.Name, Record.`Time` FROM Person INNER JOIN Record ON Person.id = Record.visitorId ORDER BY Record.`Date` ASC, Record.Time ASC")
    attr = list(curr)
    return render_template("latecome.html", attr = attr)


if __name__ == "__main__":
    app.run()
