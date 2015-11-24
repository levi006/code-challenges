
#			List Representation of Binary Trees
			 
################################################################################################

# List implementation of tree

myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]

def BinaryTree(r):
    return [r, [], []]


# Inserting a Left Child 

def insertLeft(root, newBranch):
    leftSubtree = root.pop(1)
    
    if len(leftSubtree) > 1:
        root.insert(1, [newBranch, leftSubtree, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

"""To insert a left child, we pop the (possibly empty) list that corresponds to the current left child. 
We then add the new left child and installing the old left child as the left child relative of the new one. 
This allows us to splice a new node into the tree at any position.""" 

# Inserting a Right Child 

def insertRight(root, newBranch):
    rightSubtree = root.pop(2)
    
    if len(rightSubtree) > 1:
        root.insert(2, [newBranch, [], rightSubtree])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#				Node and References Reperesentations of Binary Trees

################################################################################################

"""Our second method to represent a tree uses nodes and references. In this case we will define a class that has 
attributes for the root value, as well as the left and right subtrees. Since this representation more closely follows 
the object-oriented programming paradigm, we will continue to use this representation for the remainder of the chapter."""

class BinaryTree:

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

# To add a left child to the tree, create a new binary tree object and set the left attribute of the root to refer to this new object.
	
def insertLeft(self,newNode):

    if self.leftChild == None: #adds child to the tree
        self.leftChild = BinaryTree(newNode)
    else:
        tree = BinaryTree(newNode) #pushes the existing child down one level in the tree
        tree.leftChild = self.leftChild
        self.leftChild = tree

def getRightChild(self):
    return self.rightChild

def getLeftChild(self):
    return self.leftChild

def setRootVal(self,obj):
    self.key = obj

def getRootVal(self):
    return self.key

