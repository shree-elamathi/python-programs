'''
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went
missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of
the n + m rolls.
You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also
given the two integers mean and n.
Return an array of length n containing the missing observations such that the average value of the n + m rolls is
exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty
array. The average value of a set of k numbers is the sum of the numbers divided by k.
Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
'''
class Solution:
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        total_sum = mean * (n + m)  # Total sum of n + m rolls
        observed_sum = sum(rolls)  # Sum of the m observed rolls
        missing_sum = total_sum - observed_sum  # Sum that the n missing rolls should add up to

        # Check if the missing sum is feasible
        if missing_sum < n or missing_sum > 6 * n:
            return []  # Impossible to find valid dice rolls

        # Initialize the missing rolls with all 1's (the minimum value)
        missing_rolls = [1] * n
        remaining_sum = missing_sum - n  # The sum we still need to distribute

        # Distribute the remaining sum to the rolls
        for i in range(n):
            add = min(5, remaining_sum)  # We can add at most 5 to any roll
            missing_rolls[i] += add
            remaining_sum -= add
            if remaining_sum == 0:
                break

        return missing_rolls

rolls = [3,2,4,3]
mean = 4
n = 2
print(Solution().missingRolls(rolls,mean,n))