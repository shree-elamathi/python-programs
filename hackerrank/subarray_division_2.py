'''
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.
'''
class Solution:
    def birthday(self,s,d,m): #d -> day and m -> month
        count=0
        for i in range(len(s)-m+1):
            if sum(s[i:i+m])==d:
                count+=1
        return count
s=[2,2,1,3,2]
d=4
m=2
print(Solution().birthday(s,d,m))