'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays
are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.
'''
class Solution:
    def sortPeople(self,names,heights):
        zipped_pair=zip(heights,names)
        sort_pair=sorted(zipped_pair)
        arr1,arr2=zip(*sort_pair)
        arr2=list(arr2)
        return arr2[::-1]
names=["Mary","John","Emma"]
heights = [180,165,170]
print(Solution().sortPeople(names,heights))