# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        bank_of_vowels = []
        for alphabet in s:
            if alphabet in vowels:
                bank_of_vowels.append(alphabet)
        bank_of_vowels = bank_of_vowels[::-1]
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + bank_of_vowels.pop(0) + s[i+1:]
        return s