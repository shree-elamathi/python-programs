'''
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the
remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.
'''


class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        target_mod = total_sum % p
        if target_mod == 0:
            return 0
        mod_dict = {0: -1}
        current_sum_mod = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            current_sum_mod = (current_sum_mod + num) % p
            needed_mod = (current_sum_mod - target_mod) % p
            if needed_mod in mod_dict:
                min_length = min(min_length, i - mod_dict[needed_mod])
            mod_dict[current_sum_mod] = i
        return min_length if min_length < len(nums) else -1


nums = [3,1,4,2]
p = 6
print(Solution().minSubarray(nums,p))