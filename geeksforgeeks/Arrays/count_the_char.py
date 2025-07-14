'''
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively
it is counted as 1 occurrence.
'''


class Solution:
    def getCount(self, s, N):
        Dict = {}
        for i in range(len(s) - 1):
            if (s[i] == s[i + 1]):
                continue
            else:
                if s[i] not in Dict:
                    Dict[s[i]] = 1
                else:
                    Dict[s[i]] += 1
        if s[-1] != s[-2]:
            if s[-1] not in Dict:
                Dict[s[-1]] = 1
            else:
                Dict[s[-1]] += 1

        print(Dict)

        count = 0
        for i in Dict:
            if Dict[i] == N:
                count += 1

s = "umeaylnlfd"
N = 2
print(Solution().getCount(s,N))