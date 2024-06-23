'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such
that the absolute difference between any two elements of this subarray is less than or equal to limit.
'''
from collections import deque


class Solution:
    def longestSubarray(self, nums, limit) :
        max_deque, min_deque = deque(), deque()
        left, right, res = 0, 0, 0

        while right < len(nums):
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)

            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

nums = [8,2,4,7]
limit = 4
print(Solution().longestSubarray(nums,limit))