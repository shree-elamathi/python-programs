'''
Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.
'''
class Solution:
    def countOfElements(self, a, n, x):
        count=0
        for i in a:
            if i<=x:
                count+=1
        return count
a=[1, 2, 4, 5, 8, 10]
n=6
x=9
print(Solution().countOfElements(a,n,x))