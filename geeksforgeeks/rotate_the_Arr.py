'''
Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.
'''
class Solution:
    def leftRotate(self, arr, d):
        arr[:]=arr[d:]+arr[:d]
        return arr

arr= [1,2,3,4,5]
d=2
print(Solution().leftRotate(arr,d))