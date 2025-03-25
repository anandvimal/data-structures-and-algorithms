s = "abc"
t = "ahbgdc"
# Output: true

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         for s_char in s:
#             if s_char not in t:
#                 return False
#             else:
#                 s_index = t.index(s_char)
#                 t = t[s_index+1:]
#         return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for s_char in s:
            found = False

            for t_char in t:
                if s_char == t_char:
                    t = t[t.index(t_char)+1:]
                    found = True
                    break
            if not found:
                return False

        return True