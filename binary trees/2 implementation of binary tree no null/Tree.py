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

def deleteNode(root:Node, key:int):
    if isPlaceHolderNode(root):
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else: #node found
        #case: node haas 0/ one right child node
        if isPlaceHolderNode(root.left):
            temp:Node = root.right
            #delete(root)
            #root = root.right
            return temp
        
        #case: node has one left child node
        elif isPlaceHolderNode(root.right):
            temp:Node = root.left
            #delete(root)
            #root= root.left
            return temp
        
        temp:Node = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)
    return root

def minValueNode(root:Node):
    current:Node = root
    #search the leftmost tree
    while isPlaceHolderNode(current) == False and isPlaceHolderNode(current.left):
        current = current.left
    return current

root = getNewNode(1)
print(root.key)
print(root.left.key)
print(root.right.key)
root = insertNode(root, 2)
print(root.key)
print(root.left.key)
print(root.right.key)
root = deleteNode(root,1)
print(root.key)
print(root.left.key)
print(root.right.key)