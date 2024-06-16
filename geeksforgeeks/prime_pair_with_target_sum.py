'''
Given a number n, find out if n can be expressed as a+b, where both a and b are prime numbers. If such a pair
exists, return the values of a and b, otherwise return [-1,-1] as an array of size 2.
Note: If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, and a < c then
[a, b] is considered as our answer.
'''
import sympy


class Solution:
    def getPrimes(self,n):
        arr=[]
        for i in range(2,int(n/2)+1):
            a=i
            b=n-i
            is_primea=Solution().isprime(a)
            is_primeb=Solution().isprime(b)
            if is_primea and is_primeb:
                arr.append(a)
                arr.append(b)
                return arr
        return [-1,-1]
    def isprime(self,n):
        for i in range(2, int(n / 2) + 1):
            if (n % i == 0):
                return False
        else:
            return True



n=5
print(Solution().getPrimes(n))