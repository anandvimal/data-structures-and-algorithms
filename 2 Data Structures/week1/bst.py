class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def printInOrder(self):
        if self.value is not None:
            if self.left is not None:
                self.left.printInOrder()
            print(f"{self.value}")
            if self.right is not None:
                self.right.printInOrder()
    
    def add(self, key):
        if self.value is None:
            self.value = key
        else:
            while self is not None:
                print(f"{self.value}")
                if key > self.value :
                    if self.right is not None:
                        self = self.right
                    else:
                        self.right = Node(key)
                        break
                else: 
                    if self.left is not None:
                        self= self.left
                    else: 
                        self.left = Node(key)
                        break

            # self = Node(key)
            # print(self.value)



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right= Node(5)
    root.add(10)
    root.add(-1)
    #root.add(11)
    #root.add(12)

    print("------------")
    root.printInOrder()

