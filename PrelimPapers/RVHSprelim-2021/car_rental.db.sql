BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `RentalRecord` (
	`CustomerID`	INTEGER,
	`VIN`	TEXT,
	`StartDate`	TEXT,
	`CollectionPointID`	INTEGER NOT NULL,
	`ReturnDate`	TEXT,
	`ReturnPointID`	INTEGER,
	FOREIGN KEY(`CollectionPointID`) REFERENCES `RentalPoint`(`PointID`),
	PRIMARY KEY(`CustomerID`,`VIN`,`StartDate`),
	FOREIGN KEY(`VIN`) REFERENCES `Car`(`VIN`),
	FOREIGN KEY(`ReturnPointID`) REFERENCES `RentalPoint`(`PointID`),
	FOREIGN KEY(`CustomerID`) REFERENCES `Customer`(`CustomerID`)
);
INSERT INTO `RentalRecord` VALUES (3,'1C3LC45K38N218667','20210703',7,'20210705',4);
INSERT INTO `RentalRecord` VALUES (2,'2C3LA63H86H198110','20210703',8,'20210706',1);
INSERT INTO `RentalRecord` VALUES (5,'1C4BJWFG7EL217905','20210703',4,'20210705',5);
INSERT INTO `RentalRecord` VALUES (5,'1C4BJWFG7EL217905','20210706',5,'20210710',5);
INSERT INTO `RentalRecord` VALUES (2,'2C3LA63H86H198110','20210712',1,'20210715',1);
INSERT INTO `RentalRecord` VALUES (9,'3N1CN7AP7CL993199','20210718',1,'20210720',5);
INSERT INTO `RentalRecord` VALUES (10,'1C3LC45K38N218667','20210718',4,'','');
CREATE TABLE IF NOT EXISTS `RentalPoint` (
	`PointID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Address`	TEXT NOT NULL,
	`OpWeekDay`	TEXT NOT NULL,
	`OpStartHr`	TEXT NOT NULL,
	`OpEndHr`	TEXT NOT NULL
);
INSERT INTO `RentalPoint` VALUES (1,'Changi Airport T3','0111110','0800','1800');
INSERT INTO `RentalPoint` VALUES (2,'Changi Airport T1','1111111','0000','2400');
INSERT INTO `RentalPoint` VALUES (3,'Changi Airport T2','1111111','0800','1800');
INSERT INTO `RentalPoint` VALUES (4,'303 Orchard Road','0111110','0000','2400');
INSERT INTO `RentalPoint` VALUES (5,'6 Boon Lay Ave','0111110','0800','1800');
INSERT INTO `RentalPoint` VALUES (6,'Bukit Timah Nature Reserve','0111110','0900','2200');
INSERT INTO `RentalPoint` VALUES (7,'Singapore Zoo','0111110','0900','2200');
INSERT INTO `RentalPoint` VALUES (8,'Marina Sands','1111111','0900','2200');
INSERT INTO `RentalPoint` VALUES (9,'Sentosa Hotel W','1111111','0800','1800');
INSERT INTO `RentalPoint` VALUES (10,'Noidea Drive','0111110','0900','2200');
CREATE TABLE IF NOT EXISTS `Customer` (
	`CustomerID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`Gender`	TEXT NOT NULL CHECK("Gender" = 'M' OR "Gender" = 'F'),
	`Contact`	TEXT NOT NULL
);
INSERT INTO `Customer` VALUES (1,'Su Ming De','M','94190731');
INSERT INTO `Customer` VALUES (2,'Tan Yong Quan','M','93350642');
INSERT INTO `Customer` VALUES (3,'Qin Kai Hui','F','95967027');
INSERT INTO `Customer` VALUES (4,'Law Zheng En','M','97060128');
INSERT INTO `Customer` VALUES (5,'Goh Yi Xi','M','99634088');
INSERT INTO `Customer` VALUES (6,'Shen Rui Min','F','98022248');
INSERT INTO `Customer` VALUES (7,'Tung De Ming','M','90577667');
INSERT INTO `Customer` VALUES (8,'Chong Jun Jie','M','98259724');
INSERT INTO `Customer` VALUES (9,'Goh Siew Ming','M','90581846');
INSERT INTO `Customer` VALUES (10,'Lew Hui Wen','F','99158028');
CREATE TABLE IF NOT EXISTS `Car` (
	`VIN`	TEXT,
	`Brand`	TEXT NOT NULL,
	`VehicleType`	TEXT NOT NULL CHECK("VehicleType" = 'Sedan' OR "VehicleType" = 'Hatchback' OR "VehicleType" = 'SUV' OR "VehicleType" = 'MPV'),
	`EnergySource`	TEXT NOT NULL CHECK("EnergySource" = 'Diesel' OR "EnergySource" = 'Gasoline' OR "EnergySource" = 'Hybrid' OR "EnergySource" = 'Electricity'),
	`DailyPrice`	REAL NOT NULL,
	`Availability`	TEXT NOT NULL DEFAULT 'Available' CHECK("Availability" = 'Available' OR "Availability" = 'Unavailable'),
	PRIMARY KEY(`VIN`)
);
INSERT INTO `Car` VALUES ('1C3LC45K38N218667','Volkswagen','SUV','Diesel',321.5,'Available');
INSERT INTO `Car` VALUES ('2C3LA63H86H198110','Toyota','Sedan','Gasoline',298.1,'Available');
INSERT INTO `Car` VALUES ('1C4BJWFG7EL217905','Toyota','MPV','Hybrid',385.6,'Available');
INSERT INTO `Car` VALUES ('3N1CN7AP7CL993199','Ford Motor','Sedan','Gasoline',340.2,'Available');
INSERT INTO `Car` VALUES ('2T3ZF4DV8BW080813','Ford Motor','Hatchback','Electricity',268.6,'Available');
COMMIT;
