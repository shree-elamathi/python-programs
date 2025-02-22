'''
Given a street of N houses (a row of houses), each house having K amount of money kept inside; now there is a thief
who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. Find the
maximum money he can rob.
'''

class Solution:
    def maximizeMoney(self, N , K):
        if N < 3:
            return K
        if N % 2 !=0:
            x = (N//2)+1
        else:
            x = N//2
        val = 0
        for _ in range(x):
            val += K
        return val

N = 5
K = 10
print(Solution().maximizeMoney(N,K))
