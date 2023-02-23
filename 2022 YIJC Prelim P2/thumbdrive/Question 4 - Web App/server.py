from flask import Flask, render_template, request   
from datetime import *

app = Flask(__name__)                               

#####################################
#### do not edit above this line ####

import sqlite3

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/loans")
def loan():
    client = sqlite3.connect("SportsLoans.db")
    curr = client.execute("SELECT Name FROM Student")
    names = list(curr)
    for i in range(len(names)):
        names[i] = names[i][0]

    curr = client.execute("SELECT Name FROM Equipment")
    items = list(curr)
    for i in range(len(items)):
        items[i] = items[i][0]
    return render_template("loan.html", items= items, names = names)

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboardform.html")

@app.route("/synthesis" , methods = ["POST"])
def synthesis():
    if request.method == "POST":
        name = request.form.get("name")
        item = request.form.get("item")
        qty = request.form.get("quantity")
        sd = request.form.get("startDate")

        ed = datetime.strptime(sd, "%Y-%m-%d")+ timedelta(days=2)
        ed = ed.strftime("%Y-%m-%d")

        client = sqlite3.connect("SportsLoans.db")
        curr = client.execute("SELECT ID FROM Student WHERE Name = ?", (name,))
        sID = list(curr)[0][0]
        print(sID)

        curr = client.execute("SELECT ID FROM Equipment WHERE Name = ?", (item,))
        iID = list(curr)[0][0]

        curr = client.execute("INSERT INTO Loan (EqptID, StudentID, LoanDate, ReturnDate) VALUES (?,?,?,?)", (iID, sID, sd, ed))

        curr = client.execute("SELECT Points FROM Equipment WHERE Name = ?", (item,))
        pt = list(curr)[0][0]
        points = pt * int(qty)
        
    return render_template("success.html", name = name, rd = ed, points = points)


@app.route("/lbsynthesis", methods=["POST"])
def lbsynthesis():
    if request.method == "POST":
        name = request.form.get("name")
        client = sqlite3.connect("SportsLoans.db")
        curr = client.execute("SELECT Student.Name, SUM(Equipment.Points) FROM Student INNER JOIN Loan ON Loan.StudentID = Student.ID INNER JOIN Equipment ON Equipment.ID = Loan.EqptID WHERE Student.Name = ? GROUP BY Student.Name", (name,))
        points = list(curr)[0][1]

        curr = client.execute("SELECT Student.Name, SUM(Equipment.Points) AS s FROM Student INNER JOIN Loan ON Loan.StudentID = Student.ID INNER JOIN Equipment ON Equipment.ID = Loan.EqptID GROUP BY Student.Name ORDER BY s DESC LIMIT 3;")
        attr = list(curr)

        return render_template("leaderboard.html", attr = attr, points = points)

    else:
        return render_template("index.html")
        
        

#####################################
#### do not edit below this line ####           

app.run('127.0.0.1', port = 5000)   
#you may wish to update the port number if port 5000 has been used.    

