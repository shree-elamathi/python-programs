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

        # Using sliding window for the problem
        # using l and r pointers slide through the string
        # the idea is to calculate the changes which is len - max frequency
        # If the changes <= k then it is valid else
        # look for other substring
        while r < len(s):

            #update the hash map and max frequency
            if s[r] in hash:
                hash[s[r]] += 1
                maxf = max(maxf, hash[s[r]])
            else:
                hash.update([(s[r],1)])
                maxf = max(maxf, hash[s[r]])

            #if changes > k then reduce the substring len by moving l towards right
            # and update the hash map
            if ((r-l+1)-maxf > k):
                hash[s[l]] -= 1
                l += 1

            # if changes <= k then it is valid
            # so update the max len
            if ((r-l+1)- maxf <= k):
                maxlen = max(maxlen,r-l+1)

            r += 1

        #return max length
        return maxlen

s = "XYYX"
k = 2
print(Solution().characterReplacement(s,k))
