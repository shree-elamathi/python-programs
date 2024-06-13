'''
Given a number n, find the nth number in the Padovan Sequence.
A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1
Note: Since the output may be too large, compute the answer modulo 10^9+7.
'''
class Solution:
    def padovanseq(self,n):
        MOD = 1000000007
        if n == 0 or n == 1 or n == 2:
            return 1
        p0, p1, p2 = 1, 1, 1
        for i in range(3, n + 1):
            pnext = (p1 + p0) % MOD
            p0, p1, p2 = p1, p2, pnext
        return p2

n=4
print(Solution().padovanseq(n))