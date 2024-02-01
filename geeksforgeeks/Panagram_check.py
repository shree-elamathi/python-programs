#Given a string s check if it is "Panagram" or not.
# A "Panagram" is a sentence containing every letter in the English Alphabet.
class Solution:
    def checkPangram(self, s):
        if len(s)<26:
            return 0
        alpha='abcdefghijklmnopqrstuvwxyz'
        alphaup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(0,len(alpha)):
            if alpha[i] not in s:
                if alphaup[i] not in s:
                    return 0
        return 1
s="sdfs"
print(Solution().checkPangram(s))