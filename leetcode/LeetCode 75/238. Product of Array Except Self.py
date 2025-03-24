# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums) # make it fill with 1 for length of nums
        suffix_product = [1] * len(nums)
        result = []

        for i in range(len(nums)):
            if i == 0:
                prefix_product[i] = 1
            else:
                prefix_product[i] = prefix_product[i-1] * nums[i-1]
        #print(f"prefix_product: {prefix_product}")

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix_product[i] = 1
            else:
                suffix_product[i] = suffix_product[i+1] * nums[i+1]
        #print(f"suffix_product: {suffix_product}")

        for i in range(len(nums)):
            result.append(prefix_product[i] * suffix_product[i])
        return result
        


nums = [1,2,3,4]
# Output: [24,12,8,6]

print(Solution().productExceptSelf(nums))