class Solution:
    def minOperation(self, n):
        m=1
        a=1
        if m==n:
            return a
        else:
            m=2
            a=2
            while m<n:
                if m*2<=n:
                    print("if st:",m)
                        m=m*2
                        a+=1
                else:
                    print("else st:",m)
                    m+=1
                    a+=1
        return a,m


n = int(input("Enter the number: "))
ob=Solution()
print(ob.minOperation(n))
