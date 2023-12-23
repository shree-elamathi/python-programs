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
        val=[]
        for i in arr:
            if i+k<max(arr):
                val.append(i+k)
            else:
                if i>k:
                    val.append(i-k)
                else:
                    val.append(i+k)
        val.sort()
        for i in range(0,len(val)):
           if val[i]>val[len(val)-1]:
               val[i]=val[i]-k
        return (max(val)-min(val))


arr=[1,8,10,6,4,6,9,1]
k=7
n=8
print(Solution().getMinDiff(arr,n,k))

