N=24
##class Solution:
##    def largestPrimeFactor (self, N):
##        a=[]
##        b=[2]
##        c=[]
##        for i in range(2,N+1):
##            a.append(i)
##        print(a)
##        for j in a:
##            if (j%2==0):
##                continue
##            else:
##                b.append(j)
##        print(b)
##        for i in b:
##            if(N%i==0):
##                c.append(i)
##        print(c)
##        m=len(c)
##        print(m)
##        return (c[m-1])
##       
##


class Solution:
    def largestPrimeFactor (self, N):
        a=[2]
        for i in range(2,N+1):
            if(i%2!=0)and(N%i==0):
                a.append(i)
                break
        print(a)
        m=len(a)
        return (a[m-1])

ob = Solution()
print(ob.largestPrimeFactor(N))
        
