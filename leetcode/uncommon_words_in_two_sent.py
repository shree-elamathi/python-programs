'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
'''
class Solution:
    def uncommonFromSentences(self, s1, s2):
        res=[]
        rep=[]
        str1=s1.split(" ")
        str2=s2.split(" ")
        for i in range(len(str1)):
            if str1[i] in rep:
                continue
            if str1[i] not in str1[i+1:] and str1[i] not in str2:
                res.append(str1[i])
            if str1[i]  in str1[i + 1:]:
                rep.append(str1[i])
        for i in range(len(str2)):
            if str2[i] in rep:
                continue
            if str2[i] not in str2[i+1:] and str2[i] not in str1:
                res.append(str2[i])
            if str2[i]  in str2[i + 1:]:
                rep.append(str2[i])
        return res

s1 = "apple apple"
s2 = "banana"
print(Solution().uncommonFromSentences(s1,s2))