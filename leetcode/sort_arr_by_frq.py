'''
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple
values have the same frequency, sort them in decreasing order.
Return the sorted array.
'''
class Solution:
    def frequencySort(self,nums):
        val=list(set(nums))
        val.sort(reverse=True)
        freq=[]
        ans=[]
        for i in val:
            c=nums.count(i)
            freq.append(c)
        for _ in range(len(val)):
            x=min(freq)
            ind=freq.index(x)
            for i in range(x):
                ans.append(val[ind])
            freq[ind]=200
        return ans
nums=[1,1,2,2,2,3]
print(Solution().frequencySort(nums))