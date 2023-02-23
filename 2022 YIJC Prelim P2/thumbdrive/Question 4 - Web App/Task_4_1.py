from csv import *
from sqlite3 import *

#write program code to populate the Loan table with the data from LOAN.TXT

db = connect("SportsLoans.db")
with open("LOAN.txt") as fs:
    # Automatically closes the filestream

    data = fs.read().split("\n")

    for row in data[1:]:
        items = row.split(",")

        curr = db.execute("INSERT INTO Loan(LoanId, EqptID, StudentID, LoanDate, ReturnDate) VALUES (?,?,?,?,?)", tuple(items))
        

db.commit()
db.close()
