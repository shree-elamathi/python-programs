'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number
target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element
twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.
'''


class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = i+1
        while i<len(numbers) and j <=len(numbers):
            if i < len(numbers) and j==len(numbers):
                i+=1
                j= i+1
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]

            elif numbers[i] + numbers[j] >target:
                i += 1
                j = i+1

            else:
                j+=1

numbers = [-5,-3,0,2,4,6,8]
target = 5
print(Solution().twoSum(numbers,target))
