'''
You are given a 3-digit number n, Find whether it is an Armstrong number or not.
An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the
number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371.
Note: Return "true" if it is an Armstrong number else return "false".
'''
class Solution:
    def armarmstrongNumber(self,n):
        n=str(n)
        a=int(n[0])**3
        b=int(n[1])**3
        c=int(n[2]) ** 3
        if (a+b+c)==int(n):
            return True
        return False
n=371
print(Solution().armarmstrongNumber(n))