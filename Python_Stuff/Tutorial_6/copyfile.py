
inputFileName = input("Please enter the name of the input file: ")
outputFileName = input("Please enter the name of the output file: ")

class fileManipulator:
    def __init__(self, name):
        self.name = name
        f = open(self.name, 'r')
        self.stringContents = f.read()
        self.arrayContents = self.stringContents.split("\n")
        f.close()
    
    def updateFileObjects(self):
        f = open(self.name, 'r')
        self.stringContents = f.read()
        self.arrayContents = self.stringContents.split("\n")
        f.close()

    def updateContents(self, content):

        f = open(self.name, 'w')
        f.write(content)
        f.close()
    
    def transferContents(self, other):
        other.updateContents(self.stringContents)


file_One = fileManipulator(inputFileName)
file_Two = fileManipulator(outputFileName)

file_One.transferContents(file_Two)
