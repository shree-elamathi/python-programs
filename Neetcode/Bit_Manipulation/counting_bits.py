'''
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.
'''


class Solution:
    def countBits(self, n) :
        ans = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            ans .append(count)

        return ans


n = 4
print(Solution().countBits(n))