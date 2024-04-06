#Given an array nums of n positive integers. Find the minimum number of operations required to modify the array such
# that array elements are in strictly increasing order (nums[i] < nums[i+1]). Changing a number to greater or lesser
# than original number is counted as one operation. Note: Array elements can become negative after applying operation.
class Solution:
    def min_operations(self, nums):
        l=Solution().Lis(nums)
        return (len(nums)-l)
    def Lis(self,arr):
        dp=[]
        for i in range (len(arr)):
            dp.append(1)
        for i in range(1,len(arr)):
            for j in range(0,i):
                if (arr[i]>arr[j]) and (arr[i]-arr[j]>=i-j):
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)


nums = [10,5,5,2,4,10,3,2,7,9]
print(Solution().min_operations(nums))
