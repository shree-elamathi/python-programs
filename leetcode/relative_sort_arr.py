'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements
that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''
class Solution:
    def relativesortarr(self,arr1,arr2):
        arr1.sort()
        k=0
        for i in arr2:
            c=arr1.count(i)
            for j in range(c):
                arr1.remove(i)
            for j in range(c):
                arr1.insert(k,i)
            k+=c
        return arr1


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(Solution().relativesortarr(arr1,arr2))