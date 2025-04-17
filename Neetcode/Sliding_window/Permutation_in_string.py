'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a
substring of s2, then return true.
Both strings only contain lowercase letters.
'''


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        hashchar = {}
        for i in s1:
            if i in hashchar:
                hashchar[i] += 1
            else:
                hashchar[i] = 1

        for i in s2:
            if i in hashchar:
                hashchar[i] -= 1

        for i in hashchar:
            if hashchar[i] != 0:
                return False

        return True


s1 = "abc"
s2 = "lecabee"
print(Solution().checkInclusion(s1,s2))