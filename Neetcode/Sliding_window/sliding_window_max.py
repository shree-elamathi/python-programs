'''
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the
left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []

        l = 0

        #Traverse through the nums using a pointer
        while l <= len(nums) - k:
            val = nums[l]

            #to check the largest number in that window size k
            for i in range(k):
                if nums[l + i] > val:
                    val = nums[l + i]

            ans.append(val)
            l += 1

        return ans


nums = [1,2,1,0,4,2,6]
k = 3
print(Solution().maxSlidingWindow(nums,k))

