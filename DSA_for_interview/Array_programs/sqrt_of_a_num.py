'''
Given a positive integer n, find the square root of n. If n is not a perfect square,then return the floor value.
Floor value of any number is the greatest Integer which is less than or equal to that number
'''


class Solution:
    def floorSqrt(self, n):
        left, right = 0, n
        ans = 1
        while left <= right:
            mid = right + 1 // 2
            if mid * mid <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

n = int(input("Enter a number: "))
print(Solution().floorSqrt(n))