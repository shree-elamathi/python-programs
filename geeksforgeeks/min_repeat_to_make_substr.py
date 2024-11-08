'''
Given two strings s1 and s2. Return a minimum number of times s1 has to be repeated such that s2 is a substring
of it. If s2 can never be a substring then return -1.
Note: Both the strings contain only lowercase letters.
'''
class Solution:
    def minRepeats(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        k = (n2 // n1) + n1
        s = s1
        count = 1
        i = 0
        while i < k:
            if s.find(s2) != -1:
                return count
            else:
                count += 1
                s += s1
            i += 1
        return -1


s1 = "ww"
s2 = "www"
print(Solution().minRepeats(s1,s2))