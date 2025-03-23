#Input: s = "the sky is blue"
#Output: "blue is sky the"

input = "the sky is blue"
output = "blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.strip()
        #text = s
        words = text.split()
        #print (text)
        #print(words)
        solution = ""
        for i in range(len(words)-1, -1 , -1):
            #print(words[i], end = " ")
            solution = solution + words[i] + " "
        solution = solution.strip()
        #print(solution)
        return solution

sol = Solution()
sol.reverseWords(s= input)
print(sol.reverseWords(input))