import flask, sqlite3

from flask import render_template

app = flask.Flask(__name__, template_folder="Task2_4_Marcus_1_1/templates")


@app.route("/")
def main():
    conn = sqlite3.connect("ServiceLog.db")
    curr = conn.execute("SELECT Sender, AccessDate, AppType, `Status` FROM `Log`")
    listOfContents = list(curr)

    print(listOfContents)

    return render_template("index.html", attr = listOfContents)

if __name__ == "__main__":
    app.run()

