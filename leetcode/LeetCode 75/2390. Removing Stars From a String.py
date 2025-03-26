class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter == '*' : # star never makes into the stack
                stack.pop() # pop previous/ last item in stack
            else:
                stack.append(letter)
        result = ''.join(stack)
                
        return result

        