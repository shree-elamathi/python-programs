'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''
class Solution:
    def sort_color(self,nums):
        k=0
        for i in range(3):
            c=nums.count(i)
            for j in range(c):
                nums.remove(i)
            for j in range(c):
                nums.insert(k,i)
                k+=1
        return nums
nums=[2,0,2,1,1,0]
print(Solution().sort_color(nums))