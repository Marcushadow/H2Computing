CREATE TABLE `Device` (
	`SerialNumber`	INTEGER PRIMARY KEY,
	`Type`	TEXT CHECK (`Type` = 'Monitor' OR `Type` = 'Laptop' OR `Type` = 'Printer'),
	`Model`	TEXT,
	`Location` TEXT,
	`DateOfPurchase` TEXT,
	`WrittenOff` TEXT CHECK (WrittenOff = "TRUE" OR WrittenOff = "FALSE")
);

CREATE TABLE `Monitor` (
	`MonitorId` INTEGER PRIMARY KEY AUTOINCREMENT,
	`SerialNumber`	INTEGER,
    `DateCleaned`   TEXT,
    FOREIGN KEY (`SerialNumber`) REFERENCES `Device`
);

CREATE TABLE `Laptop` (
	`LaptopId` INTEGER PRIMARY KEY AUTOINCREMENT,
	`SerialNumber`	INTEGER,
    `WeightKg`   REAL,
    FOREIGN KEY (`SerialNumber`) REFERENCES `Device`
);

CREATE TABLE `Printer` (
	`PrinterId` INTEGER PRIMARY KEY AUTOINCREMENT,
	`SerialNumber`	INTEGER,
    `Toner`   TEXT,
    `DateChanged`   TEXT,
    FOREIGN KEY (`SerialNumber`) REFERENCES `Device`
);