import datetime, sqlite3


class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        
    def is_adult(self):
        year = datetime.date.today().year
        return (year - int(self.date_of_birth[:4])) >= 18
    
    def screen_name(self):
    
        finalName = self.full_name
        space_and_punc = [".", ",", '"', "-", "_", "'", " "]
        
        for punc in space_and_punc:
            fN = finalName.replace(punc, "")
            
            
           
        fN = finalName + self.date_of_birth[5:7] + self.date_of_birth[-2:]
        
        return finalName
            
    
class Staff(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
        
    def is_adult(self):
        return True

    def screen_name(self):
        return self.full_name + " Staff"
    
class Student(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
        
    def is_adult(self):
        return False


with open("people.txt") as fs:
    data = fs.read().strip("\n").split("\n")
    
    for i in range(len(data)):
        data[i] = data[i].split(",")
        

conn = sqlite3.connect("school.db")

for p in data:
    if(p[2] == "Person"):
        guy = Person(p[0], p[1])
    
    elif(p[2] == "Staff"):
        guy = Staff(p[0], p[1])
    
    else:
        guy = Student(p[0], p[1])
    
    FullName = p[0]
    DateOfBirth = p[1]
    ScreenName = guy.screen_name()
    IsAdult = guy.is_adult()

    curr = conn.execute("INSERT INTO People (FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?,?,?,?)", (FullName, DateOfBirth, ScreenName, IsAdult ))
    conn.commit()
    
    
conn.commit()
