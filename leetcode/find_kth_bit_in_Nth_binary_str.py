'''
Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all
the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findK(n, k):
            if n == 1:
                return '0'
            length = (1 << n) - 1
            mid = length // 2 + 1

            if k == mid:
                return '1'
            elif k < mid:
                return findK(n - 1, k)
            else:
                mirrored_k = length - k + 1
                return '0' if findK(n - 1, mirrored_k) == '1' else '1'

        return findK(n, k)


solution = Solution()
print(solution.findKthBit(3, 1))
