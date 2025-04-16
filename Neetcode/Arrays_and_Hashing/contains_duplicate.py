'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''


class Solution:
    def hasDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False


nums = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums))