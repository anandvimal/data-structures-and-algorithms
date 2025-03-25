# Example 1:

nums = [1,12,-5,-6,50,3]
k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


nums =[0,1,1,3,3]
k = 4

# nums =[9,7,3,5,6,2,0,8,1,9]
# k = 6
# Output: 5.33333

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = current_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k] #add right, sub left
            max_sum = max(current_sum, max_sum)

        return max_sum/ k    
        

#slower
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         highest_average = 0
#         sum = 0
#         average = 0
#         if len(nums) > k:
#             for i in range(len( nums)+1-k):
#                 sum = 0
#                 average = 0
#                 for j in range(k):
#                     sum += nums[j+i]
#                 average = sum/k
#                 if average > highest_average:
#                     highest_average = average
#             return highest_average
#         else:
#             for i in range(len(nums)):
#                 sum += nums[i]
#             return sum/len(nums)    
        

sol = Solution()
print(sol.findMaxAverage(nums, k))
        