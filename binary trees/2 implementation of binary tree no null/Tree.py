import math 

class Node:
    def __init__(self, key=None):
        self.key=key
        self.left = None
        self.right = None

def getNewNode(key: int):
    t:Node = Node(key)
    t.left = Node(-math.inf)
    t.right = Node(math.inf)
    return t

    pass

def isPlaceHolderNode(n :Node):
    #return n.key == math.inf or n.key == -math.inf
    return math.isinf(n.key)

def insertNode(root:Node, key:int):
    if isPlaceHolderNode(root):
        #delete(root)
        root = Node(key)
        return root
    
    if key < root.key:
        root.left = insertNode(root.left, key)
    else:
        root.right = insertNode(root.right, key)
    return root

root = getNewNode(1)
print(root.key)
print(root.left.key)
print(root.right.key)
root = insertNode(root, 2)
print(root.key)
print(root.left.key)
print(root.right.key)