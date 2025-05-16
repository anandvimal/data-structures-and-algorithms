from typing import List

def k_sum_subarrays_optimized(nums: List[int], k: int) -> int:
    count = 0
    # Initialize the map with 0 to handle subarrays that sum to 'k' 
    # from the start of the array
    prefix_sum_map = {0: 0}
    curr_prefix_sum = 0
    for num in nums:
        # Update the current prefix sum, by adding the current number
        curr_prefix_sum += num
        # If a subarray with sum 'k' is found, increment the count by the 
        # number of times that prefix sum has been seen found
        if curr_prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[curr_prefix_sum - k]
        # Update the map with the current prefix sum
        freq  = prefix_sum_map.get(curr_prefix_sum, 0)
        prefix_sum_map[curr_prefix_sum] = freq + 1
    return count 

nums = [1, 2, -1, 1, 2]
k = 3

result = k_sum_subarrays_optimized(nums, k)
print(f"Number of subarrays with sum {k}: {result}")