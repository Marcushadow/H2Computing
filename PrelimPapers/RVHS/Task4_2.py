import csv, sqlite3

with open("Teacher.csv") as fs:
    reader = csv.reader(fs, delimiter=",")
    headings = next(reader)
    client = sqlite3.connect("invigilation.db")
    
    for line in reader:
        curr = client.execute("INSERT INTO Teacher (TeacherID, Name, Department, Contact) VALUES (?,?,?,?)", tuple(line))
    client.commit()
    client.close()

with open("Venue.csv") as fs:
    reader = csv.reader(fs, delimiter=",")
    headings = next(reader)
    client = sqlite3.connect("invigilation.db")
    
    for line in reader:
        curr = client.execute("INSERT INTO Venue (VenueID, VenueName, RoomNo) VALUES (?,?,?)", tuple(line))
    client.commit()
    client.close()

with open("ExamSession.csv") as fs:
    reader = csv.reader(fs, delimiter=",")
    headings = next(reader)
    client = sqlite3.connect("invigilation.db")
    
    for line in reader:
        curr = client.execute("INSERT INTO ExamSession (ExamSessionID, SubjectName, PaperNo, VenueID, Date, StartTime, EndTime) VALUES (?,?,?,?,?,?,?)", tuple(line))
    client.commit()
    client.close()

with open("ExamDuty.csv") as fs:
    reader = csv.reader(fs, delimiter=",")
    headings = next(reader)
    client = sqlite3.connect("invigilation.db")
    
    for line in reader:
        curr = client.execute("INSERT INTO ExamDuty (ExamSessionID, TeacherID, Role) VALUES (?,?,?)", tuple(line))
    client.commit()
    client.close()
