'''
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.
'''


class Solution:
    def hammingWeight(self, n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1

        return count


n = 21
print(Solution().hammingWeight(n))