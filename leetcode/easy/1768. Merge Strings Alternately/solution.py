class Solution:

    def mergeB(self, word1:str, word2:str, length:int) -> str:
        result = ""
        for i in range(0,length):
            result += word1[i]
            result += word2[i]
        return str(result)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            result = Solution.mergeB(self, word1, word2, len(word1))
            print(result)
            return result
        elif len(word1) > len(word2):
            result = Solution.mergeB(self, word1, word2, len(word2))
            result = result + word1[len(word2):]
            print(result)
            return result
        else:
            result = Solution.mergeB(self, word1, word2, len(word1))
            result = result + word2[len(word1):]
            print(result)
            return result

        