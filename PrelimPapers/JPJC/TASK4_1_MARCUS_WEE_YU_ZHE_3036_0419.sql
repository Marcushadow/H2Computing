CREATE TABLE `Customer` (
	`Email`	TEXT,
	`FirstName`	TEXT,
	`LastName`	TEXT,
	`ContactNumber`	INTEGER,
	`DOB`	TEXT,
	`Address`	TEXT,
	PRIMARY KEY(`Email`)
);
CREATE TABLE `Product` (
	`CatalogueNumber`	INTEGER,
	`Category`	TEXT,
	`Brand`	TEXT,
	`Size`	INTEGER,
	`Fee`	REAL,
	PRIMARY KEY(`CatalogueNumber`)
);
CREATE TABLE `CustomerRental` (
	`Email`	TEXT,
	`ID`	INTEGER,
	`StartDate`	TEXT,
	`EndDate`	TEXT,
	PRIMARY KEY(`ID`),
	FOREIGN KEY(`Email`) REFERENCES `CustomerRental`(`Email`)
);
CREATE TABLE `ProductRental` (
	`ID`	INTEGER,
	`CatalogueNumber`	INTEGER,
	`Returned`	TEXT,
	FOREIGN KEY(`CatalogueNumber`) REFERENCES `ProductRental`(`CatalogueNumber`),
	PRIMARY KEY(`ID`,`CatalogueNumber`),
	FOREIGN KEY(`ID`) REFERENCES `CustomerRental`(`ID`)
);