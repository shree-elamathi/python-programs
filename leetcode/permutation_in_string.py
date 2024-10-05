'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])
        for i in range(len_s2 - len_s1):
            if s1_count == window_count:
                return True
            window_count[s2[i]] -= 1
            if window_count[s2[i]] == 0:
                del window_count[s2[i]]
            window_count[s2[i + len_s1]] += 1
        return s1_count == window_count


s1 = "ab"
s2 = "eidbaooo"
sol = Solution()
print(sol.checkInclusion(s1, s2))