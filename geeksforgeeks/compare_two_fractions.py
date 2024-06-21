'''
You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they
are equal, then return "equal".
Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )).
'''
class Solution:
    def compareFrac(self, s):
        val=[]
        val1=s[:s.index(",")]
        val2=s[s.index(",")+2:]
        for i in range(len(val1)):
            if val1[i]=="/":
                a=int(val1[:i])
                b=int(val1[i+1:])
                val.append(a/b)
                break
        for i in range(len(val2)):
            if val2[i]=="/":
                a=int(val2[:i])
                b=int(val2[i+1:])
                val.append(a/b)
                break
        if val[0]>val[1]:
            return val1
        elif val[0]<val[1]:
            return val2
        else:
            return "equal"
str = "8/1, 8/1"
print(Solution().compareFrac(str))