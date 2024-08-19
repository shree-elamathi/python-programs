'''
Given a number, reverse it and add it to itself unless it becomes a palindrome or return -1 if the number of
iterations becomes more than 5. Return that palindrome number if it becomes a palindrome else returns -1.
'''
class Solution:
    def isSumPalindrome (self, n):
        if self.ispalindrome(n):
            return n
        else:
            i=0
            while i<5:
                str_n=str(n)
                rev=int(str_n[::-1])
                n=n+rev
                if self.ispalindrome(n):
                    return n
                else:
                    i+=1
            return "-1"
    def ispalindrome(self,s):
        str_s=str(s)
        rev=str_s[::-1]
        if str_s==rev:
            return True
        return False
n=73
print(Solution().isSumPalindrome(n))