'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.
'''

class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:

            #find the middle index
            mid = low + (high - low) // 2

            #if middle value and target are equal return middle value
            if nums[mid] == target:
                return mid

            #if target is less than middle value then move the window to the left
            elif nums[mid] < target:
                low = mid + 1

            #else move the window to the right
            else:
                high = mid - 1

        #repeat the process until we find or if not found then return -1
        return -1


nums = [-1,0,2,4,6,8]
target = 4
print(Solution().search(nums,target))