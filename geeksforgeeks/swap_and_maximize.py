'''
Given an array arr[ ] of positive elements. Consider the array as a circular array, meaning the element after the
last element is the first element of the array. The task is to find the maximum sum of the absolute differences
between consecutive elements with shuffling of array elements allowed i.e. shuffle the array elements and make
[a1..an] such order that  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1| is maximized.
'''


class Solution:
    def maxSum(self, arr):
        arr.sort()
        n = len(arr)
        l, r = 0, n - 1
        rearr = []
        while l <= r:
            if l != r:
                rearr.append(l)
                rearr.append(r)
            else:
                rearr.append(l)
            l += 1
            r += 1
        max_sum = 0
        for i in range(n):
            max_sum += abs(rearr[i] - rearr[(i + 1) % n])
        return max_sum


arr = [4, 2, 1, 8]
print(Solution().maxSum(arr))
