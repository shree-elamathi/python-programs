'''
Given an array arr of size n and you have to tell whether the arr is perfect or not. An array is said to be
perfect if its reverse array matches the original array. If the arr is perfect then return True else return
False.
'''
class Solution:
    def perfectArr(self,arr,n):
        i=0
        j=n-1
        while i<=j:
            if arr[i]!=arr[j]:
                return False
            i+=1
            j-=1
        return True

arr=[1, 2, 3, 4, 1]
n=5
print(Solution().perfectArr(arr,n))