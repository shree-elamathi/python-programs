'''
A string s is called happy if it satisfies the following conditions:
s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy
strings, return any of them. If there is no such string, return the empty string "".
A substring is a contiguous sequence of characters within a string.
'''
import heapq
class Solution:
    def longestDiverseString(self, a, b, c):
        max_heap = []
        if a > 0: heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: heapq.heappush(max_heap, (-b, 'b'))
        if c > 0: heapq.heappush(max_heap, (-c, 'c'))
        result = []
        while max_heap:
            # Pick the character with the highest remaining count
            count1, char1 = heapq.heappop(max_heap)
            # If the last two characters are the same as char1, pick the next one
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break  # No other characters available to prevent consecutive repetition
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # Decrease count2 (restore negative count)
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count1, char1))  # Push char1 back for future use
            else:
                result.append(char1)
                count1 += 1  # Decrease count1 (restore negative count)
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))
        return ''.join(result)


a = 1
b = 1
c = 7
print(Solution().longestDiverseString(a,b,c))