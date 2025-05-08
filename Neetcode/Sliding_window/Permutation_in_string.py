'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a
substring of s2, then return true.
Both strings only contain lowercase letters.
'''


class Solution:
    def checkInclusion(self, s1, s2):
        val1 = 0
        for i in s1:
            val1 += ord(i)

        n = len(s1)
        val2 = 0

        l, r = 0,0
        while r <= len(s2) - n:
            if r == l + n and val2 == val1:
                return True

            elif r >= l+n:
                val2 = 0
                l += 1
                r = l

            else:
                val2 += ord(s2[r])
                r += 1

        return False

s1 = "abc"
s2 = "lecabee"
print(Solution().checkInclusion(s1,s2))