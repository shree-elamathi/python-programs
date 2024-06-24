'''
You are given a binary array nums and an integer k.
A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray
to 1, and every 1 in the subarray to 0.
Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible,
return -1.
A subarray is a contiguous part of an array.
'''
class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flip_count = 0
        is_flipped = [0] * n
        total_flips = 0
        for i in range(n):
            if i >= k:
                flip_count ^= is_flipped[i - k]
            if flip_count % 2 == nums[i]:
                if i + k > n:
                    return -1
                flip_count ^= 1
                is_flipped[i] = 1
                total_flips += 1
        return total_flips
nums=[0,1,0]
k=1
print(Solution().minKBitFlips(nums,k))