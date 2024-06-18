'''
Given an array A of N integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where
i = 0, 1, 2,., n 1.
You are allowed to rearrange the elements of the array.
Note: Since output could be large, hence module 109+7 and then print answer.
'''
class Solution:
    def Maximize(self, a, n):
        a.sort()
        res=0
        MOD=1000000007
        for i in range(n):
            res+=(a[i]*i)
        return res%MOD
a=[5, 3, 2, 4, 1]
n=5
print(Solution().Maximize(a,n))