'''
Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no
non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.
'''


class Solution:

    def nonRepeatingChar(self, s):
        rep = []
        non_rep = []
        for i in s:
            if i not in rep:
                rep.append(i)
            else:
                non_rep.append(i)
        for i in rep:
            if i not in non_rep:
                return i
        return "$"


s = "geeksforgeeks"
print(Solution().nonRepeatingChar(s))