from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left= right= zero_count= maximum_length  =0

        for right in range(len(nums)):

            if nums[right] == 0:
                zero_count +=1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1


            length = right-left + 1
            maximum_length = max(maximum_length, length)

        return maximum_length


        