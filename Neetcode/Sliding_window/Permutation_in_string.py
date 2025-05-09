'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a
substring of s2, then return true.
Both strings only contain lowercase letters.
'''


class Solution:
    def checkInclusion(self, s1, s2):

        # Create a hash map for the first string
        s1hash = {}
        n = len(s1)
        for i in s1:
            if i in s1hash:
                s1hash[i] += 1
            else:
                s1hash.update([(i,1)])

        #Travel from left to right
        l = 0
        while l <= len(s2) - n:

            #create a new hashmap everytime the left pointer moves
            s2hash = {}

            #travel within the window size of first string and update the new hashmap
            for i in range(n):
                if s2[l + i] in s2hash:
                    s2hash[s2[l + i]] += 1
                else:
                    s2hash.update([(s2[l + i], 1)])

            # if both the hashmaps are equal then return True
            #which means both the window has the same element
            if s1hash == s2hash:
                return True

            #if not shift the left pointer
            else:
                l += 1

        #If not return True after traversing from left to right
        return False

s1 = "abc"
s2 = "ccccbbbbaaaa"
print(Solution().checkInclusion(s1,s2))