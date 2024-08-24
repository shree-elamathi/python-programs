'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome,.
If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers.
'''
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        smaller, larger = num - 1, num + 1
        while True:
            smaller_str = str(smaller)
            if smaller_str == smaller_str[::-1]:
                break
            smaller -= 1
        while True:
            larger_str = str(larger)
            if larger_str == larger_str[::-1]:
                break
            larger += 1
        if num - smaller <= larger - num:
            return str(smaller)
        else:
            return str(larger)
# Example usage
solution = Solution()
print(solution.nearestPalindromic("123"))  # Output: "121"
print(solution.nearestPalindromic("1000"))  # Output: "999"

