'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
'''
class Solution:
    def count(self,steps,path):
        lvl=0
        res=0
        for i in path:
            if i=='D' and lvl==0:
                res+=1
            if i=='D':
                lvl-=1
            elif i=='U':
                lvl+=1
        return res
steps=8
path=['U','D',"D","D","U","D","U","U"]
print(Solution().count(steps,path))