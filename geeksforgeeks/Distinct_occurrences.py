#Given two strings s and t of length n and m respectively. Find the count of distinct occurrences of
# t in s as a sub-sequence modulo 109 + 7.
class solution:
    def sequencecount(self,s,t):
        MOD=(10**9)+7
        n,m=len(s),len(t)
        val=[0]*(m+1)
        val[0]=1
        for i in range(1,n+1):
            for j in range(m,0,-1):
                if s[i-1]==t[j-1]:
                    val[j]=(val[j]+val[j-1])%MOD
        return val[m]





s="banana"
t="ban"
print(solution().sequencecount(s,t))