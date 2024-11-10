''''
Given two sorted arrays a[] and b[], where each array contains distinct elements , the task is to return the elements
in the union of the two arrays in sorted order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the
arrays.
'''

class Solution:
    def findUnion(self,a,b):
        a+=b
        a=list(set(a))
        a.sort()
        return a


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(Solution().findUnion(a,b))