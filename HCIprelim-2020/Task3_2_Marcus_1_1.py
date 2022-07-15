import sqlite3
conn = sqlite3.connect("bakery.db")

with open("CAKES.txt") as fs:
    data = fs.read().strip("\n").split("\n")
    for entry in data:
        value = entry.split(",")
        curr = conn.execute("INSERT INTO Product (ProductCode, `Name`, `Location`, Price, `Type`) VALUES (?,?,?,?,'Cake')", (value[0], value[1], value[2], value[3]) )
        curr = conn.execute("INSERT INTO Cake (ProductCode, Shape, ServingSize) VALUES (?,?,?)", (value[0], value[5], value[4]) )


with open("LOAVES.txt") as fs:
    data = fs.read().strip("\n").split("\n")
    for entry in data:
        value = entry.split(",")
        curr = conn.execute("INSERT INTO Product (ProductCode, `Name`, `Location`, Price, `Type`) VALUES (?,?,?,?,'Loaf')", (value[0], value[1], value[2], value[3]) )
        curr = conn.execute("INSERT INTO Loaf (ProductCode, `Weight`) VALUES (?,?)", (value[0], value[4]) )

with open("BUNS.txt") as fs:
    data = fs.read().strip("\n").split("\n")
    for entry in data:
        value = entry.split(",")
        curr = conn.execute("INSERT INTO Product (ProductCode, `Name`, `Location`, Price, `Type`) VALUES (?,?,?,?,'Loaf')", (value[0], value[1], value[2], value[3]) )
        curr = conn.execute("INSERT INTO Bun (ProductCode, PiecesPerPackage) VALUES (?,?)", (value[0], value[4]) )

conn.commit()
conn.close()