'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''
class Solution:
    def long_palindrome(self,s):
        if len(s) == 1:
            return 1
        from collections import Counter
        char_counts = Counter(s)
        plen = 0
        odd_found = False
        for count in char_counts.values():
            if count % 2 == 0:
                plen += count
            else:
                plen += count - 1
                odd_found = True
        if odd_found:
            plen += 1
        return plen
s="abccccdd"
print(Solution().long_palindrome(s))