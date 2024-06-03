'''Given a number n, find the number of binary strings of length n that contain consecutive 1's in them.
Since the number can be very large, return the answer after modulo with 1e9+7.'''
class Solution:
    def numberOfConsecutiveOnes (self,n):
        mod=10**9+7
        p,q,r=0,1,1
        for i in range(3,n+1):
            a=(p+q)%mod
            r=(2*r+a)%mod
            p=q
            q=a
        return r
n=5
print(Solution().numberOfConsecutiveOnes(n))