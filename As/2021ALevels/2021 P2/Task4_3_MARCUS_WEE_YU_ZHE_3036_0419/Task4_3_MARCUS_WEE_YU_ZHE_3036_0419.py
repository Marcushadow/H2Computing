import flask, sqlite3
from flask import render_template

app = flask.Flask(__name__)


@app.route("/")
def main():
    return render_template("menu.html")

@app.route("/round1")
def round1():
    roundNo = 1
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT competitor.name, scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 1 ORDER BY scores.score DESC")
    attr = list(curr)

    return render_template("round.html", roundNo = roundNo, attr = attr)

@app.route("/round2")
def round2():
    roundNo = 2
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT competitor.name, scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 2 ORDER BY scores.score DESC")
    attr = list(curr)

    return render_template("round.html", roundNo = roundNo, attr = attr)

@app.route("/round3")
def round3():
    roundNo = 3
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT competitor.name, scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 3 ORDER BY scores.score DESC")
    attr = list(curr)

    return render_template("round.html", roundNo = roundNo, attr = attr)

@app.route("/meanScores")
def meanScore():
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT competitor.name, ROUND(AVG(scores.score),1) FROM competitor INNER JOIN scores ON competitor.id = scores.id GROUP BY competitor.id")
    attr = list(curr)

    return render_template("mean.html", attr = attr)

if __name__ == "__main__":
    app.run()
