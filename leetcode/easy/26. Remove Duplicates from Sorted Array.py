from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        result = []
        for item in nums:
            if item not in seen:
                seen.add(item)
                result.append(item)
        #nums = result
        nums.clear()
        nums.extend(result)
        return len(nums)
