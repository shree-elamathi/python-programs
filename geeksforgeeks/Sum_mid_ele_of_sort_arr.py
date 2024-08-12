'''
Given 2 sorted integer arrays arr1 and arr2 of the same size. Find the sum of the middle elements of two sorted
arrays arr1 and arr2.
'''
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        arr2=arr1+arr2
        arr2.sort()
        val=arr2[len(arr1)-1]+arr2[len(arr1)]
        return val
arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]
print(Solution().sum_of_middle_elements(arr1,arr2))