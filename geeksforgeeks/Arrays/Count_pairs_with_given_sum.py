'''
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum
is equal to K.
'''
class Solution:
    def getPairsCount(self, arr, n, k):
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==k:
                    count+=1
        return count
arr=[1, 5, 7, 1]
n=4
k=6
print(Solution().getPairsCount(arr,n,k))