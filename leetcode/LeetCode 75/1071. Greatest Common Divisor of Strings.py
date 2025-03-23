# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#------------------------------------------------------------------------
str1 = "ABCABC"
str2 = "ABC"

# str1 = "ABABAB"
# str2 = "ABAB"

# str1 = "LEET"
# str2 = "CODE"



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)
        if length1 < length2:
            smaller = str1
            larger = str2
        else:
            smaller = str2
            larger = str1
        # print(f"smaller: {smaller}")
        # print(f"larger: {larger}")
        solution = self.find_gcd(smaller, larger)
        return solution
    
    def find_gcd(self, smaller, larger):
        dividers_smaller = []
        dividers_larger = []
        test_s = ""
        test_l = ""
        if len(smaller) == 0:
            return ""
        for i in range(1, len(smaller)+1):
            divider_s = smaller[:i]
            # print(f"divider_s: {divider_s}")
            if len(smaller) % len(divider_s) == 0:
                multiplier_s = len(smaller) // len(divider_s)
                test_s = divider_s * multiplier_s
                # print(f"test_s: {test_s}")
                if test_s == smaller:
                    dividers_smaller.append(divider_s)
        
        for i in range(1, len(larger)+1):
            divider_l = larger[:i]
            # print(f"divider_l : {divider_l}")
            if len(larger) % len(divider_l) == 0:
                multiplier_l = (len(larger) // len(divider_l))
                test_l = divider_l * multiplier_l
                # print(f"test_l: {test_l}")
                if test_l == larger:
                    dividers_larger.append(divider_l)

        biggest_common_divider = ""
        for smaller_divider in dividers_smaller:
            if smaller_divider in dividers_larger:
                biggest_common_divider = smaller_divider


        # print(f"dividers_smaller: {dividers_smaller}")
        # print(f"dividers_larger: {dividers_larger}")

        # print(f"biggest_common_divider: {biggest_common_divider}")
        return biggest_common_divider
            
        


    

sol = Solution()
#sol.gcdOfStrings(str1, str2)
print(sol.gcdOfStrings(str1, str2))
#