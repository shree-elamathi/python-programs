'''
You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next
adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you gain
an increase in altitude with each step.
'''
class Solution:
    def maxStep(self, arr):
        max_jump=0
        i=0
        jump=0
        while i<len(arr)-1:
            if arr[i+1]>arr[i]:
                jump+=1
                i+=1
            else:
                max_jump=max(max_jump,jump)
                jump=0
                i+=1
        max_jump=max(max_jump,jump)
        return max_jump


arr = [1, 2, 2, 3, 2]
print(Solution().maxStep(arr))