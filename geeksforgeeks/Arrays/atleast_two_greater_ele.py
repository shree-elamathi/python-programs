'''
Given an array of N distinct elements, the task is to find all elements in array except two greatest elements
in sorted order.
'''
class Solution:
    def findElements(self,a, n):
        a.sort()
        return a[:len(a)-2]
a=[2, 8, 7, 1, 5]
n=5
print(Solution().findElements(a,n))