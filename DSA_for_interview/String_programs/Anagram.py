'''
Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an
anagram of each other or not. An anagram of a string is another string that contains the same characters, only the
order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2
can only contain lowercase alphabets.
Note: You can assume both the strings s1 & s2 are non-empty.
'''

class Solution:
    def areAnagrams(self, s1, s2):
        hashs1 = [0] * 26
        hashs2 = [0] * 26
        if len(s1) < len(s2):
            return False

        for char in s1:
            hashs1[ord(char) - 97] += 1

        for char in s2:
            hashs2[ord(char) - 97] += 1

        for char in s1:
            if hashs1[ord(char) - 97] != hashs2[ord(char) - 97] :
                return False
        return True


s1 = "allergy"
s2 = "allergic"
print(Solution().areAnagrams(s1, s2))