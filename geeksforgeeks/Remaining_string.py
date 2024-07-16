'''
Given a string s without spaces, a character ch and an integer count. Your task is to return the substring that
remains after the character ch has appeared count number of times.
Note:  Assume upper case and lower case alphabets are different. “”(Empty string) should be returned if it is not
possible, or the remaining substring is empty.
'''
class Solution:
    def printString(self, s, ch, count):
        if ch not in s:
            return ""
        for i in s:
            if count==0:
                break
            if i==ch:
                s=s[s.index(i)+1:]
                count-=1
        if count!=0:
            return ""
        return s

s="Thisisdemostring"
ch = 'i'
count = 3
print(Solution().printString(s,ch,count))