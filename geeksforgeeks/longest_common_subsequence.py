x=6
y=6
s1 = "ABCDGH"
s2 = "ACDGHR"
class Solution:
    def lcs(self,x,y,s1,s2):
        if x==0 or y==0:
            return 0
        elif s1[x-1]==s2[y-1]:
            return 1+ob.lcs(x-1,y-1,s1,s2)
        else:
            return max(ob.lcs(x,y-1,s1,s2),ob.lcs(x-1,y,s1,s2))

ob=Solution()
print(ob.lcs(x,y,s1,s2))

##def lcs(X, Y, m, n):
##	if m == 0 or n == 0:
##		return 0
##	elif X[m-1] == Y[n-1]:
##		return  1+lcs(X, Y, m-1, n-1)
##	else:
##		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
##
##
### Driver code
##if __name__ == '__main__':
##	S1 = "ACABBBBDBAAB"
##	S2 = "BBCCBEECDCDE"
##	print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))

