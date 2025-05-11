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

        #loop through s
        while r < n:
            if s[r] in hash:

                # if the letter is already in hash map then increase count to denote
                # we have found value in str t
                # and decrement the hash value by 1
                if hash[s[r]] > 0:
                    count += 1
                hash[s[r]] -= 1

            #if it is not in hash the add it
            else:
                hash.update([(s[r], -1)])

            #If count is equal to len(t) then we have found the substring
            # Now we try to minimize the length of substring by moving l pointer towards right
            # and update hash values, if count becomes less than len(t)
            # then we stop minimizing and expand r
            # meanwhile we store the starting index as l inorder to return the string
            # if min length is asked no need to maintain starting index instead just update the min length value
            while (count == m):
                if (r-l+1 < min_length):
                    min_length = r-l+1
                    stindex = l
                hash[s[l]] += 1
                if hash[s[l]] > 0:
                    count -= 1
                l += 1

            r += 1

        # If starting index is not even updated then there is no such string
        # so return an empty string
        if stindex == -1:
            return ""

        #If not return the string
        return s[stindex: stindex + min_length]

s = "a"
t = "a"
print(Solution().minWindow(s,t))