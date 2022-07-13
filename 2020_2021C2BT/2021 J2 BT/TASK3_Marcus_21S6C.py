

class TreeNode:
    def __init__(self, word):
        self._word = word
        self._left_ptr = None
        self._right_ptr = None

    def getWord(self):
        return self._word
    
    def setWord(self, newWord):
        self._word = newWord
    
    def getLeftPtr(self):
        return self._left_ptr
    
    def setLeftPtr(self, newLeftPtr):
        self._left_ptr = newLeftPtr

    def getRightPtr(self):
        return self._right_ptr
    
    def setRightPtr(self, newrightPtr):
        self._right_ptr = newrightPtr

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        toAdd = TreeNode(value)
        if (self.root == None):
            self.root = toAdd

        else:
            probe = self.root
            while (probe != None):
                if(probe.getWord() > value):
                    if(probe.getLeftPtr() == None):
                        probe.setLeftPtr(toAdd)
                        probe = None
                    else:
                        probe = probe.getLeftPtr()
                else:
                    if(probe.getRightPtr() == None):
                        probe.setRightPtr(toAdd)
                        probe = None
                    else:
                        probe = probe.getRightPtr()
    
    def Inorder(self):
        self.InorderTraversal(self.root)

    def InorderTraversal(self, node):
        if(node != None):
            self.InorderTraversal(node.getLeftPtr())
            print(node.getWord())
            self.InorderTraversal(node.getRightPtr())

    def Preorder(self):
        self.PreorderTraversal(self.root)
    
    def PreorderTraversal(self, node):
        if(node != None):
            print(node.getWord())
            self.PreorderTraversal(node.getLeftPtr())
            self.PreorderTraversal(node.getRightPtr())


test = BinarySearchTree()

import os
filepath = os.path.join("Additional Materials", "TEXT.txt")

with open(filepath) as fs:
    data = fs.readline().split(" ")

data[-1] = data[-1].strip("\n")

for value in data:
    test.add(value)

test.Inorder()


print("\nLast task: ")
sortedList = ["advance",
"and",
"as",
"civilization",
"consume",
"create",
"more",
"people",
"technology",
"than",
"they"
]

def craftTree(tree, arr, left, right):
    if (right >= left):
        mid = (right+left)//2
        tree.add(arr[mid])

        craftTree(tree, arr, left, mid-1)
        craftTree(tree, arr, mid+1, right)
        

newTree = BinarySearchTree()

craftTree(newTree, sortedList, 0, len(sortedList)-1)

newTree.Preorder()


