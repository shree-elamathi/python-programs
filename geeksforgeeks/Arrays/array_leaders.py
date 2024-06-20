'''
Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of
the array is considered a leader if it is greater than all the elements on its right side or if it is equal to
the maximum element on its right side. The rightmost element is always a leader.
'''
class Solution:
    def leader(self,n,arr):
        maxi=0
        res=[]
        for i in range(n-1,-1,-1):
            if arr[i]>=maxi:
                res.insert(0,arr[i])
                maxi=max(maxi,arr[i])
        return res
arr=[16,17,4,3,5,2]
n=6
print(Solution().leader(n,arr))