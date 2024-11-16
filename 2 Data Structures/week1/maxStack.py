class Stack:
    
    def __init__(self):
        self.length = 0
        self.data = []
        self.maximum = []
    
    
    def isempty(self):
        if self.length == 0:
            return True
        else:
            #print(f"data: {self.data}")
            #print(f"max : {self.maximum}")
            return False
                
    def push(self, item: str):
        if self.isempty() or item > self.maximum[0]:
            self.maximum.insert(0, item)
        else:
            pass
            #self.maximum.insert(0, self.maximum[0])
        self.data.insert(0, item)
        self.length = self.length+1
        #print(self.data)
        pass

    def pop(self):
        if self.length > 0:
            top = self.data[0]
            self.data.pop(0)
            self.maximum.pop(0)
            self.length = self.length-1
            #print(self.data)
            print(top)
            return top
        else:
            #return False
            pass
        
    def big(self):
        #print(f"length: {self.length}")
        if self.length > 0:
            top = self.maximum[0]
            print(top)
            #return top


# mystack = Stack()
# print(mystack.isempty())
# mystack.push(1)
# mystack.push(2)
# mystack.push(1)
# mystack.big()
# mystack.pop()
# print(mystack.isempty())


if __name__ == "__main__":
    mystack = Stack()
    times = int(input())
    for i in range(0,times):
        cmd = input()
        if cmd == "pop":
            mystack.pop()
        elif cmd == "max":
            mystack.big()
        elif cmd.startswith("push"):
            cmd = cmd[4:]
            # print(f"pushing cmd: {cmd}")
            mystack.push(cmd)