'''
A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array
together at any location.
'''
class Solution:
    def minSwaps(self, nums):
        n=len(nums)
        k=sum(nums)
        if k==0 or k==n:
            return 0
        extended_nums=nums*2
        cur_ones=sum(extended_nums[:k])
        max_ones=cur_ones
        for i in range(1,n):
            cur_ones=cur_ones-extended_nums[i-1]+extended_nums[i+k-1]
            max_ones=max(max_ones,cur_ones)
        return k-max_ones

nums = [0,1,0,1,1,0,0]
print(Solution().minSwaps(nums))