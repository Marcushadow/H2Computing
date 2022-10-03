class Node:
    def __init__(self, value):
        self.value = value
        self.leftPtr = None
        self.rightPtr = None
        
    def getValue(self):
        return self.value
    
    def setValue(self, newValue):
        self.value = newValue
        
    def getLeftPtr(self):
        return self.leftPtr
    
    def setLeftPtr(self, newLeftPtr):
        self.leftPtr = newLeftPtr
        
    def getRightPtr(self):
        return self.rightPtr
    
    def setRightPtr(self, newRightPtr):
        self.rightPtr = newRightPtr
        
 
class BSTree:

    def __init__(self, rootNode = None):
        self.root = rootNode
    
    def Insert(self, value):
        tempNode = Node(value)
    
        if(self.root == None):
            self.root = tempNode
            
        else:
            probe = self.root
            
            while(probe != None):
                if(value > probe.value):
                    if(probe.getRightPtr() == None):
                        probe.setRightPtr(tempNode)
                        probe = None
                    else:
                        probe = probe.getRightPtr()
                
                else:
                    if(probe.getLeftPtr() == None):
                        probe.setLeftPtr(tempNode)
                        probe = None
                    else:
                        probe = probe.getLeftPtr()

    def ReverseOrder(self, tree):
        
        if tree != None:
            self.ReverseOrder(tree.getRightPtr())
            print(tree.value)
            self.ReverseOrder(tree.getLeftPtr())

    def Search(self, value):
        probe = self.root
        found = False
        while probe != None and found == False:
            if(probe.value == value):
                found = True
            else:
                if(probe.value > value):
                    probe = probe.getLeftPtr()
                
                else:
                    probe = probe.getRightPtr()
            
        return found

    def count(self, tree):

        if(tree == None):
            return 0
        else:
            return 1 + self.count(tree.getLeftPtr()) + self.count(tree.getRightPtr())

        
        
            
test = BSTree()

import os
filepath = os.path.join("Additional Material", "INSERTTOTREE.txt")

with open(filepath) as fs:
    data = fs.read().split("\n")

    for entry in data:
        if entry != "":
            test.Insert(entry)


print("\nCOming in reverse order")
test.ReverseOrder(test.root)

print("\nCOunt")
print(test.count(test.root))


print("\nFinding")
filepath = os.path.join("Additional Material", "SEARCHINTREE.txt")
with open(filepath) as fs:
    data = fs.read().split("\n")

    for entry in data:
        if entry != "":
            print(entry, test.Search(entry))
             