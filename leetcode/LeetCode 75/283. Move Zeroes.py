nums = [0,1,0,3,12]
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        count = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
                holder = nums[i]
                nums[i] = 0
                nums[index] = holder
                index += 1
        #print(nums)
        return nums

sol = Solution()    
print(sol.moveZeroes(nums))