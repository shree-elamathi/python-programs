'''
Given an unsorted array of integers arr[], and a target tar, determine the number of subarrays whose elements sum up
to the target value.
'''


class Solution:
    def subArraySum(self, arr, tar):
        count = 0
        cumulative_sum = 0
        sum_map = {0: 1}
        for num in arr:
            cumulative_sum += num
            if (cumulative_sum - tar) in sum_map:
                count += sum_map[cumulative_sum - tar]
            if cumulative_sum in sum_map:
                sum_map[cumulative_sum] += 1
            else:
                sum_map[cumulative_sum] = 1
        return count


arr = [10, 2, -2, -20, 10]
tar = -10
print(Solution().subArraySum(arr,tar))