'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i]+nums[j] == target
and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
'''

class Solution:
    def twoSum(self, nums, target) :
        val=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    val.append(i)
                    val.append(j)
        return val


nums = [3,4,5,6]
target = 7
print(Solution().twoSum(nums,target))
