CREATE TABLE Student(
	MatricNo TEXT PRIMARY KEY,
	`Class` TEXT,
	IndexNo INTEGER,
	Gender TEXT CHECK( Gender IN ("M","F"))
);

CREATE TABLE Candidate(
	CandidateNo INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT,
	Slogan TEXT,
	PortraitLink TEXT
);

CREATE TABLE Vote(
	MatricNo TEXT,
	CandidateNo INTEGER,
	
	FOREIGN KEY (MatricNo) REFERENCES Student(MatricNo),
	FOREIGN KEY (CandidateNo) REFERENCES Candidate(CandidateNo),
	PRIMARY KEY (MatricNo, CandidateNo)
);