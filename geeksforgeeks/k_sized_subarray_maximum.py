'''
Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.
'''
class Solution:
    def max_of_subarrays(self,k,arr):
        res=[]
        i=0
        while i<=len(arr)-k:
            max_val=-1
            for l in range(k):
                x=arr[i+l]
                max_val=max(max_val,x)
            res.append(max_val)
            i+=1
        return res

k = 4
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(Solution().max_of_subarrays(k,arr))

