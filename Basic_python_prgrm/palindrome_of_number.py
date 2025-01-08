#To check whether a number is a palindrome
class Solution:
    def checkPalindrome(self, n):
        rev = 0
        temp = n
        while (temp > 0):
            rem = int(temp % 10)
            rev = (rev * 10) + rem
            temp = temp // 10
        if (rev == n):
            return True
        return False

n=1123211
print(Solution().checkPalindrome(n))