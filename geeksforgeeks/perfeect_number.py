'''
Given a number n, check if a number is perfect or not. A number is said to be perfect if sum of all its factors
excluding the number itself is equal to the number.
'''

import math
class Solution:
    def isPerfectNumber(self, n):
        x = self.allFactors(n)
        sum=0
        for i in x:
            if (i!=n):
                sum+=i
        if sum==n:
            return True
        return False
    def allFactors(self, N):
        arr=[]
        i=1
        while i<=math.sqrt(N):
            if (N%i==0):
                if(N//i!=i):
                    arr.append(i)
                    arr.append(N//i)
                else:
                    arr.append(i)
            i+=1
        return arr

n = int (input("Enter a number: "))
print(Solution().isPerfectNumber(n))