'''
Given two strings S (length m) and P (length n), the task is to find the smallest substring in S that contains all
characters of P, including duplicates. If no such substring exists, return “-1”. If multiple substrings of the same
length are found, return the one with the smallest starting index.
'''


class Solution:
    def smallest_window(self, s, p):
        lens = len(s)
        lenp = len(p)

        if lens < lenp:
            return -1

        hashP = [0] * 256
        hashS = [0] * 256

        for char in p:
            hashP[ord(char)] += 1

        start = 0
        start_indx = -1
        min_len = float('inf')
        count = 0

        for j in range(lens):
            hashS [ord(s[j])] += 1

            if hashP[ord(s[j])] !=0 and hashS[ord(s[j])] <= hashP[ord(s[j])]:
                count += 1

            if count == lenp:
                while hashS[ord(s[start])] > hashP[ord(s[start])] or hashP[ord(s[start])] == 0:
                    if hashS[ord(s[start])] > hashP[ord(s[start])]:
                        hashS[ord(s[start])] -= 1
                        start += 1

                lenn = j - start + 1
                if min_len > lenn:
                    min_len = lenn
                    start_indx = start

        if start_indx == -1:
            return -1

        return s[start_indx : start_indx + min_len]

s = "timetopractice"
p = "toc"
print(Solution().smallest_window(s, p))
