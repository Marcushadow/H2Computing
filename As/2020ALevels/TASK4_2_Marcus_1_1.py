import sqlite3


con = sqlite3.connect('equipment2.db')

with open("MONITORS.txt") as fs:
    data = fs.read()
    dataArr = data.split("\n")[:-1]
    for vrow in dataArr:
        row = vrow.split(",")
        con.execute("INSERT INTO Device (SerialNumber, `Type`, Model, `Location`, DateOfPurchase, WrittenOff ) VALUES (?,'Monitor',?,?,?,?)", (int(row[0]),  row[1], row[2], row[3], row[4]))
        con.execute("INSERT INTO Monitor (SerialNumber, DateCleaned) VALUES (?,?)", (int(row[0]), row[5]))
    
    con.commit()

with open("LAPTOPS.txt") as fs:
    data = fs.read()
    dataArr = data.split("\n")[:-1]
    for vrow in dataArr:
        row = vrow.split(",")
        con.execute("INSERT INTO Device (SerialNumber, `Type`, Model, `Location`, DateOfPurchase, WrittenOff) VALUES (?,'Laptop',?,?,?,?)", (int(row[0]), row[1], row[2], row[3], row[4]))
        con.execute("INSERT INTO Laptop (SerialNumber, WeightKg) VALUES (?,?)", (int(row[0]), row[5]))
    
    con.commit()

with open("PRINTERS.txt") as fs:
    data = fs.read()
    dataArr = data.split("\n")[:-1]
    for vrow in dataArr:
        row = vrow.split(",")
        con.execute("INSERT INTO Device (SerialNumber, `Type`, Model, `Location`, DateOfPurchase, WrittenOff) VALUES (?,'Printer',?,?,?,?)", (int(row[0]), row[1], row[2], row[3], row[4]))
        con.execute("INSERT INTO Printer (SerialNumber, Toner, DateChanged) VALUES (?,?,?)", (int(row[0]), row[5], row[6]))
    
    con.commit()



con.close()

