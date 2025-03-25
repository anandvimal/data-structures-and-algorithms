# Example 1:
arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for item in arr:
            if item in map:
                map[item] += 1
            else:
                map[item] = 1
        #print(f"map: {map}")

        values = []
        for key in map:
            if map[key] in values:
                return False
            else:
                values.append(map[key])
        return True
            

Solution().uniqueOccurrences(arr)