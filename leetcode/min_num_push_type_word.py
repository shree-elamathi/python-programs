'''
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to
form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time
to type "a", two times to type "b", and three times to type "c" .
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to
any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of
times the keys will be pushed to type the string word.
Return the minimum number of pushes needed to type word after remapping the keys.
An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to
any letters.
'''
import heapq
from collections import Counter
class Solution:
    def minimumPushes(self,word):
        # Count frequency of each character
        frequency_map = Counter(word)

        # Create a max heap based on character frequency
        max_heap = [(-freq, char) for char, freq in frequency_map.items()]
        heapq.heapify(max_heap)

        count = 0
        j = 1

        # Calculate minimum pushes based on character priority
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq = -freq  # Convert back to positive frequency

            if j <= 8:
                count += freq
            elif j <= 16:
                count += freq * 2
            elif j <= 24:
                count += freq * 3
            else:
                count += freq * 4

            j += 1

        return count
word = "abcde"
print(Solution().minimumPushes(word))
