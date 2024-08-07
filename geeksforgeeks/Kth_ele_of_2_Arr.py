'''
Given two sorted arrays arr1 and arr2 and an element k. The task is to find the element that would be at the kth
position of the combined sorted array.
'''
class Solution:
    def kthElement(self, k, arr1, arr2):
        new_arr=arr1+arr2
        new_arr.sort()
        return new_arr[k-1]

arr1=[2, 3, 6, 7, 9]
arr2= [1, 4, 8, 10]
k=5
print(Solution().kthElement(k,arr1,arr2))