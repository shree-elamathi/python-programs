'''
Given a positive integer n. Your task is to return the count of set bits.
'''


class Solution:
    def setBits(self, n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count


n = 13
print(Solution().setBits(n))
