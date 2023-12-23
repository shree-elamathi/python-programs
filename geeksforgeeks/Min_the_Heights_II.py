#Given an array arr[] denoting heights of N towers and a positive integer K.
# For each tower, you must perform exactly one of the following operations exactly once.
# Increase the height of the tower by K.
# Decrease the height of the tower by K.
# Find out the minimum possible difference between the height of the shortest and tallest towers after you
# have modified each tower.You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower.
# After the operation, the resultant array should not contain any negative integers.
class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        for i in range(0,len(arr)):
            if i<=k:
                arr[i]=arr[i]+k
            else:
                arr[i]=arr[i]-k
        return arr[len(arr)-1]-arr[0]
arr=[1,5,8,10]
k=2
n=5
print(Solution().getMinDiff(arr,n,k))

