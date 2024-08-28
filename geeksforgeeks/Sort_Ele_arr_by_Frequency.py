'''
Given an array of integers arr, sort the array according to the frequency of elements, i.e. elements that have
higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.
'''
class Solution:
    def sortByFreq(self,arr):
        dict=[[] for _ in range(len(arr))]
        arr.sort()
        for i in arr:
            freq=arr.count(i)
            lst=dict[freq]
            lst.append(i)
        sorted_arr=[]
        for i in range(len(arr)-1,-1,-1):
            for k in dict[i]:
                sorted_arr.append(k)
        return sorted_arr


arr =  [5, 5, 4, 6, 4]
print(Solution().sortByFreq(arr))