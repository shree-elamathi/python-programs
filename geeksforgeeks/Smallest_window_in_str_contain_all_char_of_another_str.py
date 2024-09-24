'''
Given two strings s and p. Find the smallest window in the string s consisting of all the characters(including
duplicates) of the string p.  Return "-1" in case there is no such window present. In case there are multiple such
windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets.
'''
class Solution:
    def smallestWindow(self, s, p):
        m = len(s)
        n = len(p)

        # If p is longer than s, it's impossible to find a valid window
        if n > m:
            return "-1"

        # Frequency count of characters in p
        p_count = [0] * 26
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        s_count = [0] * 26  # To count characters in the current window
        count = 0  # Count of characters matched with p
        start = 0  # Start of window
        min_len = float('inf')  # Track the minimum length of the valid window
        min_start = 0  # Start index of the minimum length window

        for end in range(m):
            # Include current character in the window
            s_count[ord(s[end]) - ord('a')] += 1

            # If s[end] is a valid character from p and the count in the window is <= count in p, we have a match
            if s_count[ord(s[end]) - ord('a')] <= p_count[ord(s[end]) - ord('a')]:
                count += 1

            # When all characters from p are matched (including duplicates)
            while count == n:
                window_len = end - start + 1

                # Check if this window is the smallest so far
                if window_len < min_len:
                    min_len = window_len
                    min_start = start

                # Try to shrink the window from the left
                s_count[ord(s[start]) - ord('a')] -= 1

                # If removing s[start] from the window reduces the count of matched characters, reduce count
                if s_count[ord(s[start]) - ord('a')] < p_count[ord(s[start]) - ord('a')]:
                    count -= 1
                start += 1

        # If no valid window is found, return "-1"
        if min_len == float('inf'):
            return "-1"

        # Return the smallest window from the original string s
        return s[min_start:min_start + min_len]
