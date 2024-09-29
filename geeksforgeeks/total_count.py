'''
You are given an array arr[] of positive integers and a threshold value k. For each element in the array, divide it
into the minimum number of small integers such that each divided integer is less than or equal to k. Compute the total
number of these integer across all elements of the array.
'''
class Solution:
    def totalCount(self, k, arr):
        val_count=0
        for i in arr:
            if i<=k:
                val_count+=1
            else:
                x=i//k
                y=i%k
                val_count+=x
                if y>0:
                    val_count+=1
        return val_count


k = 4
arr = [10, 2, 3, 4, 7]
print(Solution().totalCount(k,arr))