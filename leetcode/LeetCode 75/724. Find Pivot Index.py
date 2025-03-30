from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        first_sum = second_sum =0
        for i in range(len(nums)):
            print(i)
            first_sum = sum(nums[:i])
            second_sum = sum(nums[i+1:])
            print(f"first_sum: {first_sum}")
            print(f"second_sum: {second_sum}")
            if first_sum == second_sum:
                return i
        return -1


# longer but can be faster. fails when 0 is pivot index.
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
        
#         half = len(nums)//2
#         print(f"total size: {len(nums)},  half size: {half}")

#         # calculate first half sum
#         first_sum = sum(nums[:half]) 
#         print(f"{nums[:half]}  sum: {sum(nums[:half])}")
#         # calculate second half sum
#         second_sum = sum(nums[half+1:])
#         print(f"{nums[half:]}  sum: {sum(nums[half+1:])}")
#         divider = half
#         if first_sum == second_sum:
#             return divider
#         elif first_sum < second_sum:
#             while first_sum < second_sum and divider < len(nums):
#                 divider +=1
#                 next_item = nums[divider]
#                 first_sum += next_item
#                 second_sum -= next_item
#         elif first_sum > second_sum:
#             while first_sum > second_sum and divider >= 0:
#                 divider -=1
#                 previous_item = nums[divider]
#                 first_sum -= previous_item
#                 second_sum += previous_item
#         else:
#             print("Logic error why?")
#         if first_sum == second_sum:
#             return divider
#         else:
#             return -1
