'''
Given a non-negative integer n. Reverse the bits of n and print the number obtained after reversing the bits.
Note:  The actual binary representation of the number is being considered for reversing the bits, no leading 0’s
are being considered.
'''

class Solution:
    def reverseBits(self,n):
        rev = 0
        while (n):
            rev <<= 1
            if n & 1 == 1:
                rev = rev ^ 1
            n >>= 1
        return rev

n = 11
print(Solution().reverseBits(n))