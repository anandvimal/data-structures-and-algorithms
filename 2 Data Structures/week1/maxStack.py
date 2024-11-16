class Stack:
    
    def __init__(self):
        self.length = 0
        self.data = []
        self.max = []
    
    def max(self):
        if len(self.data) > 0:
            return self.data[0]
    
    def isempty(self):
        if self.length == 0:
            return True
        else:
            print(f"data: {self.data}")
            print(f"max : {self.max}")
            return False
                
    def push(self, item: int):
        if self.isempty() or item > self.max[0]:
            self.max.insert(0, item)
        else:
            self.max.insert(0, self.max[0])
        self.data.insert(0, item)
        self.length = self.length+1
        print(self.data)
        pass

    def pop(self):
        if self.length > 0:
            top = self.data[0]
            self.data.pop(0)
            self.max.pop(0)
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


