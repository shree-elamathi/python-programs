'''
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and
n / 2 closing brackets ']'.
A string is called balanced if and only if:
It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.
Return the minimum number of swaps to make s balanced.
'''


class Solution:
    def minSwaps(self, s):
        balance = 0
        max_imbalance = 0

        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)
        return (max_imbalance + 1) // 2


s = "][]["
print(Solution().minSwaps(s))