'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome,.
If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers.
'''


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def generate_palindromes(n):
            """Generate potential palindrome candidates."""
            length = len(n)
            candidates = set()

            # Case 1: Palindromes with the same length
            first_half = n[:(length + 1) // 2]
            for delta in [-1, 0, 1]:
                new_half = str(int(first_half) + delta)
                if new_half:
                    if length % 2 == 0:
                        palindrome = new_half + new_half[::-1]
                    else:
                        palindrome = new_half + new_half[-2::-1]
                    if palindrome != n:  # Avoid adding the number itself
                        candidates.add(palindrome)

            # Case 2: Palindromes with length +- 1
            candidates.add('1' * (length + 1))  # e.g., '1001' for '999'
            candidates.add('9' * (length - 1))  # e.g., '999' for '1000'

            return candidates

        num = int(n)
        palindromes = generate_palindromes(n)

        closest = None
        min_diff = float('inf')

        for p in palindromes:
            if p:  # Ensure p is not an empty string
                p = int(p)
                diff = abs(p - num)
                if diff < min_diff or (diff == min_diff and p < closest):
                    min_diff = diff
                    closest = p

        return str(closest)


# Example usage
solution = Solution()
print(solution.nearestPalindromic("123"))  # Output: "121"
print(solution.nearestPalindromic("1000"))  # Output: "999"

