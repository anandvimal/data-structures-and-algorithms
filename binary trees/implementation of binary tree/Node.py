from queue import Queue

# from queue import Queue
# q = Queue()
# # The key methods available are:
# qsize() # - Get the size of the queue
# empty() # - Check if queue is empty
# full() # - Check if queue is full
# put(item) # - Put an item into the queue
# get() # - Remove and return an item from the queue
# join() # - Block until all tasks are processed


class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,root, data:int):
        if root.data == None :
            print("root is none inserting data here")
            root = Node(data=data)
            return root
        
        q = Queue()
        q.put(root)

        while q.empty() == False:
            temp = q.get()
            
            if temp.left != None:
                q.put(temp.left)
            else:
                temp.left = Node(data=data)
                return root
            
            if temp.right != None:
                q.put(temp.right)
            else:
                temp.right = Node(data=data)
                return root
            


        

root = Node() # creatinng a empty tree, just empty root.
print(root.data)
root = root.insert(root, 1)
root = root.insert(root, 2)
root = root.insert(root, 3)
root = root.insert(root, 4)
root = root.insert(root, 5)
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)