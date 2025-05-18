'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n]
inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer
that appears more than once.
'''


class Solution:
    def findDuplicate(self, nums):
        hash = {}
        for i in nums:
            if i not in hash:
                hash.update({i:1})
            else:
                return i


nums = [1,2,3,2,2]
print(Solution().findDuplicate(nums))