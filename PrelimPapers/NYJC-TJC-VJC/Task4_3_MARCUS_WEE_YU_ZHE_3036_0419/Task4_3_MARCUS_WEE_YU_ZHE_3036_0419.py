import flask, sqlite3

from flask import render_template, request, flash

app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/latecomers")
def latecome():
    client = sqlite3.connect("../Task4.db")
    curr = client.execute("SELECT Person.Name, Record.`Time` FROM Person INNER JOIN Record ON Person.id = Record.visitorId ORDER BY Record.`Date` ASC, Record.Time ASC")
    attr = list(curr)
    client.close()
    return render_template("latecome.html", attr = attr)

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/submitted", methods=["POST"])
def synthesis():
    if(request.method=="POST"):
        try:
            Id = request.form.get("VisitorID")
            Direction = request.form.get("Direction")
            Date="2022-10-05"
            Time="0722"

            client = sqlite3.connect("../Task4.db")
            curr = client.execute("INSERT INTO Record (Date, Time, Type, visitorId) VALUES (?,?,?,?)", (Date, Time,Direction, int(Id)))
            # client.commit()
            client.close()
            msg = "Successfully Added"
            
        except:
            msg = "Error uploading"
            
    return render_template("form.html", msg = msg)


if __name__ == "__main__":
    app.run()
