'''
Given a boolean 2D array, consisting of only 1's and 0's, where each row is sorted. Return the 0-based index of the
first row that has the most number of 1s. If no such row exists, return -1.
'''
class Solution:
    def rowWithMax1s(self,arr):
        c=0
        ind=0
        j=0
        for i in arr:
            co=i.count(1)
            if co>c:
                c=co
                ind=j
            j+=1
        if c==0:
            return -1
        return ind

arr = [[0, 0], [1, 1]]
print(Solution().rowWithMax1s(arr))
