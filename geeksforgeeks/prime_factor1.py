N=72
class Solution:
    def largestPrimeFactor (self, N):
        a=[2]
        i=2
        while i<=N:
            if (i%2!=0)and(N%i==0):
                a.append(i)
                i+=1
                break
            i+=1
            print(i)
        print(a)
        m=len(a)
        return (a[m-1])

ob=Solution()
print(ob.largestPrimeFactor(N))
