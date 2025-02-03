'''
Given a string s, find the length of the longest substring with all distinct characters.
'''

'''
In this approach I have marked the previous of that character and moved the start position to that position when I 
encounter it's repeating value and we continuously update the max length value. 
'''
class Solution:
    def longestUniqueSubstr(self, s):
        if len(s) <= 1:
            return len(s)
        n = len(s)
        res = 0
        vis = [-1] * 26
        start = 0
        for end in range(n):
            start = max(start, vis[ord(s[end]) - ord('a')] + 1)
            res = max(res, end - start + 1)
            vis[ord(s[end]) - ord('a')] = end
        return res


s = "geeksforgeeks"
print(Solution().longestUniqueSubstr(s))
