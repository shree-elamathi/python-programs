n=11
numerator = [3,2,4,1,1,2,1,4,1,1,1]
denominator = [5,4,5,2,3,4,3,5,2,5,1]
class Solution:
    def countFractions(self, n, numerator, denominator):
        a=[]
        ans=0
        for i in range(0,n):
            a.append(numerator[i]/denominator[i])
        for i in range(0,n):
            for j in range(i+1,n):
                sum=a[i]+a[j]
                if sum==1:
                    sum=0
                    ans+=1
                else:
                    sum=0
        return ans

ob=Solution()
print(ob.countFractions(n,numerator,denominator))

