s=input("Enter the string: ")
class Solution:
    def distinctSubsequences(self, S):
        n=len(S)
        print(n)
        a=[]
        a.append(s)
        for i in s:
            if i not in a:
                a.append(i)
        for i in range(0,n):
            for j in range(i+1,n):
                print(s[i],s[j])
                e=s[i],s[j]
                if e not in a:
                    a.append(e)
        print(len(a)+1)

ob=Solution()
ob.distinctSubsequences(s)