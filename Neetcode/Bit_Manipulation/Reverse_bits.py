'''
Given a non-negative integer n. Reverse the bits of n and print the number obtained after reversing the bits.
Note:  The actual binary representation of the number is being considered for reversing the bits, no leading 0’s
are being considered.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        width = 32
        rev = 0
        for _ in range(width):
            rev <<= 1
            rev |= n & 1
            n >>= 1
        return rev

n = 21
print(Solution().reverseBits(n))