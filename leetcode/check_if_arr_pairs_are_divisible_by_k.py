'''
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.
'''


class Solution:
    def canArrange(self, arr, k):
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        return remainder_count[0] % 2 == 0


arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
print(Solution().canArrange(arr,k))