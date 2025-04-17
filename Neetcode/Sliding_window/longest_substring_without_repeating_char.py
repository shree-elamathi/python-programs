'''
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        maxlength = 0
        n = len(s)
        hashchar = {}
        l = r = 0
        while r < n :
            if s[r] in hashchar:
                if hashchar[s[r]] >= l:
                    l = hashchar[s[r]] + 1
            hashchar[s[r]] = r
            maxlength = max(maxlength, r - l + 1 )
            r += 1

        return maxlength


s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"
print(Solution().lengthOfLongestSubstring(s))