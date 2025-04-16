'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = [0] * 26
        hasht = [0] * 26

        if len(s) != len(t):
            return False

        for char in s:
            hashs[ord(char) - 97] += 1

        for char in t:
            hasht[ord(char) - 97] += 1

        for char in s:
            if hashs[ord(char) - 97] != hasht[ord(char) - 97]:
                return False

        return True

s = "racecar"
t = "carrace"
print(Solution().isAnagram(s,t))