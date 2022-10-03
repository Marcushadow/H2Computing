CREATE TABLE `Teacher` (
	`TeacherID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Department`	TEXT,
	`Contact`	INTEGER
);
CREATE TABLE `Venue` (
	`VenueID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`VenueName`	TEXT,
	`RoomNo`	TEXT
);
CREATE TABLE `ExamSession` (
	`ExamSessionID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`SubjectName`	TEXT,
	`PaperNo`	INTEGER,
	`VenueID`	INTEGER,
	`Date`	TEXT,
	`StartTime`	TEXT,
	`EndTime`	TEXT,
	FOREIGN KEY(`VenueID`) REFERENCES `Venue`(`VenueID`)
);
CREATE TABLE `ExamDuty` (
	`ExamSessionID`	INTEGER,
	`TeacherID`	INTEGER,
	`Role`	TEXT CHECK(Role IN ('PaperCoordinator', 'Invigilator', 'Relief', 'RestroomDuty', 'Reserve')),
	FOREIGN KEY(`ExamSessionID`) REFERENCES `ExamSession`(`ExamSessionID`),
	PRIMARY KEY(`ExamSessionID`,`TeacherID`),
	FOREIGN KEY(`TeacherID`) REFERENCES `Teacher`(`TeacherID`)
);