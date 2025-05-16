from typing import List

class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sum_range(self, i: int, j: int) -> int:
        if i ==0:
            return self.prefix_sum[j]
        return self.prefix_sum[j] - self.prefix_sum[i-1]


# Example usage
nums = [1, 2, 3, 4, 5]
sum_between_range = SumBetweenRange(nums)
result = sum_between_range.sum_range(1, 3)  # Sum from index 1 to 3
print(f"Sum between range (1, 3): {result}")  # Output: 9 (2 + 3 + 4)