CREATE TABLE Product (
    ProductCode VARCHAR(60) PRIMARY KEY,
    `Name` VARCHAR(60),
    `Type` TEXT CHECK (`Type` IN ('Cake','Loaf','Bun')),
    `Location` TEXT CHECK (`Location` IN ('North', 'South', 'East', 'West')),
    Price REAL 
);

CREATE TABLE Cake (
    CakeID INTEGER PRIMARY KEY AUTOINCREMENT,
    ServingSize INTEGER,
    Shape TEXT CHECK (Shape IN ('Square', 'Circle', 'Roll')),
    ProductCode VARCHAR(60),
    FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
);

CREATE TABLE Loaf (
    `Weight` REAL,
    ProductCode VARCHAR(60),
    FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
);

CREATE TABLE Bun (
    PiecesPerPackage INTEGER,
    ProductCode VARCHAR(60),
    FOREIGN KEY (ProductCode) REFERENCES Product(ProductCode)
)