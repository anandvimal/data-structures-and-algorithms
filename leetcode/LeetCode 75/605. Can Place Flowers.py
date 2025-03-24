# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1: 
            if flowerbed[0] == 0:
                count += 1
                return count >= n
        elif len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                return count >= n
            return count >= n

        for flower_position in range(len(flowerbed)):
            if flower_position == 0:
                if flowerbed[flower_position] == 0 and flowerbed[flower_position+1] == 0:
                    flowerbed[flower_position] = 1
                    count += 1
            elif flower_position > 0 and flower_position < len(flowerbed)-1:
                if flowerbed[flower_position-1] == 0 and flowerbed[flower_position] ==0 and flowerbed[flower_position+1] == 0:
                    flowerbed[flower_position] = 1
                    count += 1
            elif flower_position == len(flowerbed)-1:
                if flowerbed[flower_position-1] ==0 and flowerbed[flower_position] == 0:
                    flowerbed[flower_position] = 1
                    count += 1
        #print(f"flowerbed: {flowerbed}")
        #print(f"count: {count}")
        return count >= n
    
# flowerbed = [1,0,0,0,1]
# n = 1

# flowerbed = [1,0,0,0,1]
# n = 2

# flowerbed = [0]
# n =1

flowerbed = [0, 0]
flowerbed = [0, 1]
n =1
sol = Solution()    
print(sol.canPlaceFlowers(flowerbed, n))
        
