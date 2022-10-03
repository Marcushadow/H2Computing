import sqlite3

client = sqlite3.connect("JPFashion.db")

with open("CUSTOMER.TXT") as fs:
    data = fs.read().split("\n")[1:]
    for entry in data:
        info = entry.split(",")
        curr = client.execute("INSERT INTO Customer (Email, FirstName, LastName, ContactNumber, DOB, Address) VALUES (?,?,?,?,?,?)", tuple(info))

with open("PRODUCT.TXT") as fs:
    data = fs.read().split("\n")[1:]
    for entry in data:
        info = entry.split(",")
        curr = client.execute("INSERT INTO Product (CatalogueNumber, Category, Brand, Size, Fee) VALUES (?,?,?,?,?)", tuple(info))

with open("PRODUCTRENTAL.TXT") as fs:
    data = fs.read().split("\n")[1:]
    for entry in data:
        info = entry.split(",")
        curr = client.execute("INSERT INTO ProductRental (ID, CatalogueNumber, Returned) VALUES (?,?,?)", tuple(info))

with open("CUSTOMERRENTAL.TXT") as fs:
    data = fs.read().split("\n")[1:]
    for entry in data:
        info = entry.split(",")
        curr = client.execute("INSERT INTO CustomerRental (ID, Email, StartDate, EndDate) VALUES (?,?,?,?)", tuple(info))
client.commit()
client.close()      

        
