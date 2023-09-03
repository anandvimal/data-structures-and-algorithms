class Stack:
    
    def __init__(self):
        self.length = 0
        self.data = []
    
    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False
                
    def push(self, item: str):
        self.data.insert(0, item)
        self.length = self.length+1
        print(self.data)
        pass

    def pop(self):
        if self.length > 0:
            top = self.data[0]
            self.data.pop(0)
            self.length = self.length-1
            print(self.data)
            return top
        else:
            return False


mystack = Stack()
print(mystack.isempty())
mystack.push(1)
mystack.push(2)
mystack.push(1)
mystack.pop()
print(mystack.isempty())



