'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
'''


class Solution:
    def topKFrequent(self, nums, k) :
        hashdict = {}
        ans = []
        for num in nums:
            if num not in hashdict:
                hashdict[num] = 0

        for num in nums:
            hashdict[num] += 1

        sorted_dict = dict(sorted(hashdict.items(), key=lambda item: item[1], reverse=True))

        for i in range(k):
            key = next(iter(sorted_dict))
            sorted_dict.pop(key)
            ans.append(key)
        return ans


nums = [2,3,3,3,4,4]
k = 2
print(Solution().topKFrequent(nums,k))