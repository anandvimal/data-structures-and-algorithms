# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1 = {}
        map2 = {}
        result1 = []
        result2 = []
        result =[]
        
        for item in nums1:
            if item in map1:
                map1[item] += 1
            else:
                map1[item] = 1
        
        for item in nums2:
            if item in map2:
                map2[item] += 1
            else:
                map2[item] = 1  

        #print(f"map1: {map1}")
        #print(f"map2: {map2}")

        for item in nums1:
            if item not in map2:
                result1.append(item)
        
        for item in nums2:
            if item not in map1:
                result2.append(item)

        result1 = list(set(result1))
        result2 = list(set(result2))
        result = [result1, result2]
        
        #print(f"result: {result}")
        return result

Solution().findDifference(nums1, nums2)