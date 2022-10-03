import sqlite3

conn = sqlite3.connect("bakery.db")

with open("CAKES.TXT") as fs:
    data = fs.read().strip("\n").split("\n")
    
    for product in data:
        params = product.split(",")
        ProductCode, Name, Location, Price, ServingSize, Shape  = params
        Price = float(Price)
        ServingSize = int(ServingSize)
        
        curr = conn.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES (?,?,'Cake',?,?)", (ProductCode, Name, Location, Price))
        curr = conn.execute("INSERT INTO Cake(ProductCode, ServingSize, Shape) VALUES (?,?,?)",(ProductCode, ServingSize, Shape))

with open("LOAVES.TXT") as fs:
    data = fs.read().strip("\n").split("\n")
    
    for product in data:
        params = product.split(",")
        ProductCode, Name, Location, Price, Weight  = params
        Price = float(Price)
        Weight = float(Weight)
        
        curr = conn.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES (?,?,'Loaf',?,?)", (ProductCode, Name, Location, Price))
        curr = conn.execute("INSERT INTO Loaf(ProductCode, Weight) VALUES (?,?)", (ProductCode, Weight))
        
with open("BUNS.TXT") as fs:
    data = fs.read().strip("\n").split("\n")
    
    for product in data:
        params = product.split(",")
        ProductCode, Name, Location, Price, PiecesPerPackage  = params
        Price = float(Price)
        PiecePerPackage = int(PiecesPerPackage)
        
        curr = conn.execute("INSERT INTO Product(ProductCode, Name, Type, Location, Price) VALUES (?,?,'Bun',?,?)", (ProductCode, Name, Location, Price))
        curr = conn.execute("INSERT INTO Bun(ProductCode, PiecesPerPackage) VALUES (?,?)", (ProductCode, PiecesPerPackage))
    
conn.commit()

conn.close()