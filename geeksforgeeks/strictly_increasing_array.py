#Given an array nums of n positive integers. Find the minimum number of operations required to modify the array such
# that array elements are in strictly increasing order (nums[i] < nums[i+1]). Changing a number to greater or lesser
# than original number is counted as one operation. Note: Array elements can become negative after applying operation.
class Solution:
    def min_operations(self, nums):
        count=0
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums==sorted(nums):
                return 0
            return 1
        else:
            val=min(nums)
            ind=nums.index(val)
            count+=ind
            for i in range(ind+1,len(nums)):
                if nums[i-1]<nums[i]:
                    continue
                else:
                    count+=1
                    nums[i]=nums[i-1]+1
        return count


nums = [1, 1, 1, 1]
print(Solution().min_operations(nums))
