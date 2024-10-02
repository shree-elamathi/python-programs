'''
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''
class Solution:
    def arrayRankTransform(self,arr):
        arr1=list(set(arr))
        arr1.sort()
        for i in range(len(arr)):
            arr[i]=(arr1.index(arr[i]))+1
        return arr


arr = [100,100,100]
print(Solution().arrayRankTransform(arr))