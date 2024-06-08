'''
You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element
extra added in between. Return the index of the extra element.
Note: 0-based indexing is followed.
'''
class Solution:
    def findextra(self,n,a,b):
        for i in range(len(b)):
            if a[i] != b[i]:
                return i
        return len(a) - 1
n=7
a=[2,4,6,8,9,10,12]
b=[2,4,6,8,10,12]
print(Solution().findextra(n,a,b))
