from typing import List
# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = total_zeros = length = 0
        max_length = 0
        k = 1
        for right in range(len(nums)):
            
            if nums[right] == 0:
                total_zeros +=1
            
            while( k < total_zeros):
                if nums[left] == 0:
                    total_zeros -= 1
                left +=1
            
            length = right-left +1
            max_length = max( max_length, length)
        return max_length-1