def compute_prefix_sums(nums):
    # start by adding first number to the prefix sums array.
    prefix_sum = [nums[0]]
    # for all remaining indexes, add nums[i] to the cumulative sum
    # from the previous index.
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])