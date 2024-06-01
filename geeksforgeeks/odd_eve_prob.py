'''Given a string s of lowercase English characters, determine whether the summation of x and y is EVEN or ODD.
where:

x is the count of distinct characters that occupy even positions in the English alphabet and have even frequency.
y is the count of distinct characters that occupy odd positions in the English alphabet and have odd frequency.
Ex: string = "ab" here 'a' has an odd(1) position in the English alphabet & has an odd(1) frequency in the string so a is odd but b has an even(2) position in the English alphabet & has odd(1) frequency so it doesn't count(since string doesn't have 2 b's) so the final answer x + y = 1+0 = 1(odd) would be "ODD".

Note: Return "EVEN" if the sum of x & y is even otherwise return "ODD".'''
class Solution:
    def odd_eve(self,s):
        x=0
        y=0
        alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",'o','p','q','r','s','t','u','v','w','x','y','z']
        lst=[]
        for i in s:
            if i not in lst:
                lst.append(i)
                num=s.count(i)
                val=alph.index(i)+1
                if val%2==0 and num%2==0:
                    x+=1
                if val%2!=0 and num%2!=0:
                    y+=1
        if (x+y)%2==0:
            return "EVEN"
        return "ODD"

s="abbbcc"
print(Solution().odd_eve(s))