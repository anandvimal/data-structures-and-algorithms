class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reverse = ""
        for i in range(len(original)-1, -1, -1):
            #print(i)
            #print(original[i])
            reverse += original[i]
        #print(f"reverse = {reverse}")
        if original==reverse:
            print(True)
            return True
        else:
            print(False)
            return False

y = Solution()
y.isPalindrome(x=5555)

        