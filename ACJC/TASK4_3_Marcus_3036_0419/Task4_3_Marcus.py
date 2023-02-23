import flask, sqlite3
from flask import render_template, request


app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/new")
def form():
    return render_template("form.html")

@app.route("/newOne", methods = ["POST"])
def newEntry():
    if(request.method == "POST"):
        bookID = request.form.get("bookID")
        title = request.form.get("title")
        price = request.form.get("price")

        db = sqlite3.connect("../Task4.db")
        curr = db.execute("SELECT COUNT(*) FROM copies WHERE bookID = ? GROUP BY bookID", (bookID,))
        if(len(list(curr)) == 0):
            num = 1
        else:
            num = 1 + int(list(curr)[0][0])
        copyID = "{:0>4}".format(str(num))

        curr = db.execute("INSERT INTO copies (copyID, bookID) VALUES (?,?)", (copyID, bookID))

        curr = db.execute("INSERT INTO books (bookID, title, price) VALUES (?,?,?)", (bookID, title, price))

        db.commit()
        db.close()
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
