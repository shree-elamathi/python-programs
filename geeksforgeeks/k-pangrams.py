'''
Given a string str and an integer k, return true if the string can be changed into a pangram after at most k
operations, else return false.
A single operation consists of swapping an existing alphabetic character with any other lowercase alphabetic character.
Note - A pangram is a sentence containing every letter in the english alphabet.
'''
class Solution:
    def kPangram(self,string, k):
        x=string.replace(" ","")
        if len(x)<26:
            return False
        alpha='abcdefghijklmnopqrstuvwxyz'
        left=[]
        for i in alpha:
            if i not in string:
                left.append(i)
        if len(left)<=k:
            return True
        return False

string="aaaaaaaaaaaaaaaaaaaaaaaaaa"
k=25
print(Solution().kPangram(string,k))