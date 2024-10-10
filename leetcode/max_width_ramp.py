'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a
ramp is j - i. Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums,
return 0.
'''
class Solution:
    def maxWidthRamp(self, nums):
        ramp=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>=nums[i]:
                    ramp=max(ramp,(j-i))
        return ramp


nums = [6,0,8,2,1,5]
print(Solution().maxWidthRamp(nums))