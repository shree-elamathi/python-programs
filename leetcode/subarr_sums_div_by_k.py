'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum
divisible by k.
'''
class Solution:
    def no_of_subarr(self,nums,k):
        count=0
        for i in range(len(nums)):
            if nums[i]%k==0:
                count+=1
            for j in range(i+1,len(nums)):
                arr=nums[i:j+1]
                if sum(arr)%k==0:
                    count+=1
        return count


nums=[5]
k=9
print(Solution().no_of_subarr(nums,k))