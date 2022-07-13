import sqlite3 

class ServiceRecord:
    def __init__(self, Sender, AccessDate, status, AppType = ""):
        self.Sender = Sender
        self.AccessDate = AccessDate
        self.Status = status
        self.AppType = AppType
    
    def isSuccess(self):
        return self.Status == 200
    
    def getAppType(self):
        return self.AppType


conn = sqlite3.connect("ServiceLog.db")

with open("LOG.txt") as fs:
    data = fs.read()
    data = data.strip("\n").split("\n")
    
    for entry in data:
        contents = entry.split(" ")
        temp = ServiceRecord(*contents)

        if(len(contents) == 3):
            curr = conn.execute("INSERT INTO `Log` (Sender, AccessDate, `Status`) VALUES (?,?,?)", tuple(contents))
        else:
            curr = conn.execute("INSERT INTO `Log` (Sender, AccessDate, `Status`, AppType) VALUES (?,?,?,?)", tuple(contents))
    
    conn.commit()
conn.close()


