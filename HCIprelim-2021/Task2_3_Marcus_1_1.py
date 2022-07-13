from Task2_2_Marcus_1_1 import ServiceRecord

class AppServiceRecord(ServiceRecord):
    def __init__(self, Sender, AccessDate, status, AppType = ""):
        super().__init__(Sender, AccessDate, status, AppType)
    
    def getAppType(self):
        if(self.AppType == "WA"):
            return "WHATSAPP"
        elif(self.AppType == "FB"):
            return "FACEBOOK MESSENGER"
        else:
            return "NOTHING"
    
    def getSuccess(self):
        if(self.isSuccess()):
            return "SUCCESS"
        else:
            return "FAILED"

class SmsServiceRecord(ServiceRecord):
    def __init__(self, Sender, AccessDate, status, AppType = "SHORT MESSAGE SERVICE"):
        super().__init__(Sender, AccessDate, status, AppType)
    
    def getAppType(self):
        return "SHORT MESSAGE SERVICE"
    
    def getSuccess(self):
        if(self.isSuccess()):
            return "SUCCESS"
        else:
            return "FAILED"