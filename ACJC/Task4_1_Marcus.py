import sqlite3

db = sqlite3.connect("Task4.db")

with open("books_data.txt") as fs:
    data = fs.read().split("\n")
    for item in data:
        info = item.split(",")
        curr = db.execute("INSERT INTO books (bookID, title, price) VALUES (?,?,?)", tuple(info))

        
with open("copies_data.txt") as fs:
    data = fs.read().split("\n")
    for item in data:
        info = item.split(",")

        curr = db.execute("INSERT INTO copies (copyID, bookID) VALUES (?,?)", (info[0],info[1]))

        
db.commit()
db.close()
