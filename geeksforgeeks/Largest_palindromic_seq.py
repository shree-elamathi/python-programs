s= "abba"
##def ispalindrome(s):
##    t=s[::-1]
##    print(t)
##    a=[]
##    for i in range(0,len(s)):
##        if s[i]==t[i]:
##             a.append(s[i])
##    for i in range(0,len(a)):
##        print(a[i],end="")
##
##ispalindrome(s)
    

##t=s[::-1]
##print(t)
##a=[]
##def ispalindrome(s):
##    for i in range(0,len(t)):
##        print(s[i])
##        for j in range(1,len(s)):            
##            print(s[j])
##            if s[i]==s[j]:
##                a.append(s[i])
##                return a+
##        
##
##print(ispalindrome(s))
##a=0
##b=[]
##n=len(s)-1
##class solution:
##    def ispalindrome(self,s,a,n):
##        if a==len(s) or n==-1:
##            return
##        elif s[a]==s[n]:
##            print("a=",a)
##            print("n=",n)
##            ob.ispalindrome(s,a+1,n-1)
##            b.append(s[a])
##        else:
##            b.clear()
##            a=1
##            ob.ispalindrome(s,a,n-1)
##            a+=1
##        for i in range(0,len(b)):
##            print(b[i],end=" ")
##ob=solution()
##ob.ispalindrome(s,a,n)
class solution:
    def check(self):
        b=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and len(b)==0:
                    ob.ispalindrome(i,j,s,b)
        
    def ispalindrome(self,i,j,s,b):
        if i==j:
            b.append(s[i])
            ob.ans(b)
        elif s[i]==s[j]:
            b.append(s[i])
            ob.ispalindrome(i+1,j-1,s,b)
        else:
            b.clear()
        
    def ans(self,b):
        c=[]
        c=b[len(b)-2::-1]
        for x in c:
            b.append(x)
        for y in b:
            print(y,end="")
              

ob=solution()
ob.check()
                  
            
        
        
