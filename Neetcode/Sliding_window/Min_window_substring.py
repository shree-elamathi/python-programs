'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates,
is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
'''

class Solution:
    def minWindow(self, s, t):
        n = len(s)
        m = len(t)
        min_length = n + 1
        count = 0
        stindex = -1

        hash = {}

        #insert the values of t in hash
        for i in t:
            if i in hash:
                hash[i] += 1
            else:
                hash.update([(i,1)])

        l,r = 0,0

        while r < n:
            if s[r] in hash:
                if hash[s[r]] > 0:
                    count += 1
                hash[s[r]] -= 1
            else:
                hash.update([(s[r], -1)])

            while (count == m):
                if (r-l+1 < min_length):
                    min_length = r-l+1
                    stindex = l
                hash[s[l]] += 1
                if hash[s[l]] > 0:
                    count -= 1
                l += 1

            r += 1

        if stindex == -1:
            return ""
        return s[stindex: stindex + min_length]

s = "a"
t = "a"
print(Solution().minWindow(s,t))