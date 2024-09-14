'''
You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a
bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.
'''


class Solution:
    def longestSubarray(self, nums):
        max_val = max(nums)
        longest_length = 0
        current_length = 0
        for num in nums:
            if num == max_val:
                current_length += 1
                longest_length = max(longest_length, current_length)
            else:
                current_length = 0
        return longest_length


nums = [1, 2, 3, 3, 2, 2]
print(Solution().longestSubarray(nums))
