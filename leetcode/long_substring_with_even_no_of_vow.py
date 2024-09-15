'''
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is,
'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
'''


class Solution:
    def findTheLongestSubstring(self, s):
        bitmask = 0
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        first_occurrence = {0: -1}
        max_len = 0

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                bitmask ^= (1 << vowel_to_bit[char])
            if bitmask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i

        return max_len

s = "eleetminicoworoep"
print(Solution().findTheLongestSubstring(s))