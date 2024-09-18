'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
'''
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums)
        return '0' if largest_num[0] == '0' else largest_num


nums=[10,2]
print(Solution().largestNumber(nums))