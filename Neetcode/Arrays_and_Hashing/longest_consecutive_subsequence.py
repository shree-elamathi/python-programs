'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous
element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
'''


class Solution:
    def longestConsecutive(self, nums) :
        arr = list(set(nums))
        length = 0
        arr.sort()
        temp = 1
        for i in range(len(arr)-1):
            if arr[i+1] == arr[i] + 1:
                temp += 1
            else:
                length = max(length , temp)
                temp = 1

        length = max(length, temp)
        return length


nums = [0,3,2,5,4,6,1,1]
print(Solution().longestConsecutive(nums))