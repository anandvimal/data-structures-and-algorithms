'''
First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like ] in ](), or closes the wrong opening bracket, like } in ()[}. 
If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like ( in {}([]. 
If there are no mistakes, text editor should inform the user that the usage of brackets is correct.
'''

class Stack:
    
    def __init__(self):
        self.length = 0
        self.data = []
    
    def isempty(self):
        if self.length == 0:
            #return "Success"
            return True
        else:
            #print(self.data)
            return False
                
    def push(self, item: str):
        self.data.insert(0, item)
        self.length = self.length+1
        #print(self.data)
        pass

    def pop(self):
        if self.length > 0:
            top = self.data[0]
            self.data.pop(0)
            self.length = self.length-1
            #print(self.data)
            return top
        else:
            return False


def find_unbalanced_opening(code: str):
    opening_brackets = ['(','[','{']
    closing_brackets = [')',']','}']

    # closing_brackets = ['(','[','{']
    # opening_brackets = [')',']','}']
    
    mystack = Stack()
    counter =0
    is_open_position = 0

    for char in code:
        counter +=1
        if (char in opening_brackets) :
            if mystack.isempty():
                is_open_position = counter

        if char in opening_brackets:
            mystack.push(char)
        elif char in closing_brackets:
            if mystack.isempty():
                return is_open_position
            top = mystack.pop()
            if (top == '[' and char != ']') or (top == '{' and char != '}') or (top == '(' and char != ')'):
                # return counter+1
                pass
            elif (top == '[' and char == ']') or (top == '{' and char == '}') or (top == '(' and char == ')'):
                # counter=counter-2
                pass
        if mystack.isempty() and is_open_position > 0:
            is_open_position =0

    if mystack.isempty():
        return True
    else:
        return is_open_position


def find_unbalanced_closing(code: str):
    opening_brackets = ['(','[','{']
    closing_brackets = [')',']','}']

    # closing_brackets = ['(','[','{']
    # opening_brackets = [')',']','}']
    
    mystack = Stack()
    counter =0
    is_open_position = 0

    for char in code:
        counter +=1
        if (char in closing_brackets):
            if mystack.isempty():
                is_open_position = counter

        if char in opening_brackets:
            mystack.push(char)
        elif char in closing_brackets:
            if mystack.isempty():
                return is_open_position
            top = mystack.pop()
            if (top == '[' and char != ']') or (top == '{' and char != '}') or (top == '(' and char != ')'):
                # return counter+1
                is_open_position = counter
                return is_open_position
                pass
            elif (top == '[' and char == ']') or (top == '{' and char == '}') or (top == '(' and char == ')'):
                # counter=counter-2
                pass

        if mystack.isempty() and is_open_position > 0:
            is_open_position =0

    if mystack.isempty():
        return True
    else:
        return is_open_position





if __name__ == "__main__":
    code = input()
    result_opening = find_unbalanced_opening(code=code)
    result_closing = find_unbalanced_closing(code=code)

    if result_closing == True and result_opening == True: #can be numbers or True
        print("Success")
    elif result_closing:
        print(result_closing)
    else:
        print(result_opening)


