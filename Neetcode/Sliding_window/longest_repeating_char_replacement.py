'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k
characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one
distinct character.
'''


class Solution:
    def characterReplacement(self, s, k):
        maxlen = 0
        l, r = 0,0
        maxf = 0
        hash = {}

        while r < len(s):

            if s[r] in hash:
                hash[s[r]] += 1
                maxf = max(maxf, hash[s[r]])
            else:
                hash.update([(s[r],1)])
                maxf = max(maxf, hash[s[r]])

            if ((r-l+1)-maxf > k):
                hash[s[l]] -= 1
                l += 1

            if ((r-l+1)- maxf <= k):
                maxlen = max(maxlen,r-l+1)

            r += 1

        return maxlen

s = "XYYX"
k = 2
print(Solution().characterReplacement(s,k))
