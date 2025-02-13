'''
Given a non-empty array arr[] of integers, find the top k elements which have the highest frequency in the array. If
two numbers have the same frequencies, then the larger number should be given more preference.
'''


class Solution:
    def topKFrequent(self, arr, k):
        dict = {}
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        res = []
        d = sorted(dict.keys())[::-1]
        max1 = max(dict.values())
        while (k > 0):
            for i in d:
                if dict[i] == max1:
                    if k > 0:
                        res.append(i)
                    k -= 1
            max1 = max1 - 1
        return res


arr = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
print(Solution().topKFrequent(arr, k))
