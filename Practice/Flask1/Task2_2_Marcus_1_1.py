
import sqlite3


class ServiceRecord:

    def __init__(self, Sender, AccessDate, Status, AppType = ""):
        self.Sender = Sender
        self.AccessDate = AccessDate
        self.Status = Status
        self.AppType = AppType
   
    def isSuccess(self):
        return self.Status == 200
       
    def getAppType(self):
        return self.AppType
        
        
conn = sqlite3.connect("ServiceLog.db")
with open("LOG.txt") as fs:
    data = fs.read().strip("\n").split("\n")
    
    for line in data:
        entry = line.split(" ")
        Sender = entry[0]
        AccessDate = entry[1]
        Status = int(entry[2])
        
        if(len(entry) > 3):
            AppType = entry[3]
            instance = ServiceRecord(Sender, AccessDate, Status, AppType)
            curr = conn.execute("INSERT INTO Log (Sender, AccessDate, Status, AppType) VALUES (?,?,?,?)", (Sender, AccessDate, Status, AppType))
            conn.commit()
        else:
            instance = ServiceRecord(Sender, AccessDate, Status)
            curr = conn.execute("INSERT INTO Log (Sender, AccessDate, Status) VALUES (?,?,?)", (Sender, AccessDate, Status))
            conn.commit()


conn.close()
        
    
    
        
    