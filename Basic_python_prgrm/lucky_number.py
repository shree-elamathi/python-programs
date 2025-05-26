'''
Jack has been interested in numerology for a while and has learned how to calculate a lucky number for a given
word using the rules below:

Each alphabet in the word has an ASCII value (where 'A' = 65, 'B' = 66, ..., 'Z' = 90, 'a' = 97, etc.).

Each letter in the word is assigned a 1-based index (i.e., the first letter has index 1, the second letter has
index 2, and so on).

The lucky number is calculated as follows:

Multiply each character’s ASCII value by its 1-based index.

Include this product in the sum only if either the index or the ASCII value (or both) are odd.
'''

class Solution:
    def luckyNumber(self, s):
        arr = []
        sum = 0

        for i in s:
            arr.append(ord(i))

        for i in range(1,len(arr) + 1):
            if (i%2) != 0 or (arr[i - 1] % 2 ) != 0:
                sum += (arr[i - 1] * i)


        return sum


s = "JAMES"
print(Solution().luckyNumber(s))