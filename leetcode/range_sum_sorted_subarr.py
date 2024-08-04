'''
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous
subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the
answer can be a huge number return it modulo 109 + 7.
'''
class Solution:
    def rangeSum(self,nums,n,left,right):
        MOD=1000000007
        sub_sum=[]
        for i in range(n):
            sum=nums[i]
            sub_sum.append(sum)
            for j in range(i+1,n):
                sum+=nums[j]
                sub_sum.append(sum)
        sub_sum.sort()
        res=0
        for i in range((left-1),right):
            res+=sub_sum[i]
        return (res%MOD)


nums = [1,2,3,4]
n = 4
left = 3
right = 4
print(Solution().rangeSum(nums,n,left,right))