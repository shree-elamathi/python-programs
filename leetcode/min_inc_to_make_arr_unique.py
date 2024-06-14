'''
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and
increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.
'''
class Solution:
    def minIncrementForUnique(self,nums):
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return count
nums=[3,1,2,2,1,7]
print(Solution().minIncrementForUnique(nums))