'''
Given an array of bird sightings where every element represents a bird type id, determine the id of the most
frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
'''
class Solution:
    def migratoryBirds(self,arr):
        types=set(arr)
        print(types)
        c=0
        for i in types:
            x=arr.count(i)
            if x>c:
                c=x
                val=i
        return val
arr=[1,1,2,2,3]
print(Solution().migratoryBirds(arr))