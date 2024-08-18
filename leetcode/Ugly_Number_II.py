'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
'''


class Solution:
    def nthUglyNumber(self, n):
        ugly = [0] * n
        ugly[0] = 1

        i2 = i3 = i5 = 0
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

            if ugly[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if ugly[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        return ugly[-1]
n=10
print(Solution().nthUglyNumber(n))