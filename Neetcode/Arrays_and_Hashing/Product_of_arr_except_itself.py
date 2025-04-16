'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums
except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
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


nums = [1,2,4,6]
print(Solution().productExceptSelf(nums))