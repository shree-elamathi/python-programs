'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the
original list of strings.
Please implement encode and decode
'''

class Solution:

    def encode(self, strs) :
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) :
        res = []
        i = 0
        while i< len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            j += 1
            res.append(s[j : j+length])
            i = j+length
        return res

strs = ["neet","code","love","you"]
s = Solution().encode(strs)
print(s)
print(Solution().decode(s))
