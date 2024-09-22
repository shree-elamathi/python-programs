'''
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.
NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.
'''


class Solution:
    def longestPrefixSuffix(self, s: str) -> int:
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[-1]


sol = Solution()
s = "ababcababa"
print(sol.longestPrefixSuffix(s))
