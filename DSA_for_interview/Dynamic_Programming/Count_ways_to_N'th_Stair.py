'''
There are n stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair
or 2 stairs at a time. Count the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n = 4:- {1 2 1},{2 1 1},{1 1 2} are considered same.
'''
class Solution:
    def climbStairsOrderDoesNotMatter(self, n):
        prev1 = 1
        prev2 = 1
        for _ in range(2,n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1

n = 4
print(Solution().climbStairsOrderDoesNotMatter(n))