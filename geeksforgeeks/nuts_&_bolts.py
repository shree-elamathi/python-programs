'''
Given a set of n nuts & bolts. There is a one-on-one mapping between nuts and bolts. You have to Match nuts
and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means
the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is
bigger/smaller.
The elements should follow the following order: { !,#,$,%,&,*,?,@,^ }
Note: Make all the required changes directly in the given arrays, output will be handled by the driver code.
'''
class Solution:
    def nutsandbolts(self,n,nuts,bolts):
        order=['!','#','$','%','&','*','?','@','^']
        j=0
        for i in range(len(order)):
            if j==n:
                break
            if order[i]==nuts[j]:
                j+=1
                continue
            elif order[i] in nuts:
                ind=nuts.index(order[i])
                val=nuts[j]
                nuts[j]=order[i]
                nuts[ind]=val
                j+=1
        for i in range(n):
            if nuts[i] in bolts:
                ind=bolts.index(nuts[i])
                val=bolts[i]
                bolts[i]=nuts[i]
                bolts[ind]=val


n=5
nuts=['@', '%', '$', '#', '^']
bolts=['%', '@', '#', '$','^']
print(Solution().nutsandbolts(n,nuts,bolts))