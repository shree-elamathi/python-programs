'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Concatenate s and its reverse with a special character in between
        concat = s + "#" + s[::-1]

        # Create the KMP table (partial match table)
        kmp_table = [0] * len(concat)

        # Build the KMP table for the concatenated string
        for i in range(1, len(concat)):
            j = kmp_table[i - 1]
            while j > 0 and concat[i] != concat[j]:
                j = kmp_table[j - 1]
            if concat[i] == concat[j]:
                j += 1
            kmp_table[i] = j

        # The length of the longest palindromic prefix
        longest_palindromic_prefix_length = kmp_table[-1]

        # Characters to add in front of s to make it a palindrome
        to_add = s[longest_palindromic_prefix_length:][::-1]

        # Return the shortest palindrome by adding the necessary characters in front
        return to_add + s


# Example usage:
sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))
print(sol.shortestPalindrome("abcd"))
