'''
Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the
elements of nums except nums[i].
'''
class Solution:
    def productExceptSelf(self, nums):
        pro=1
        pro_arr=[0]*len(nums)
        for i in nums:
            if i!=0:
                pro=pro*i
        c_of_z=nums.count(0)
        if c_of_z>1:
            return [0]*len(nums)
        elif c_of_z==1:
            ind=nums.index(0)
            pro_arr[ind]=pro
        else:
            for i in range(len(nums)):
                pro_arr[i]=pro//nums[i]
        return pro_arr

nums = [10, 3, 5, 6, 2]
print(Solution().productExceptSelf(nums))