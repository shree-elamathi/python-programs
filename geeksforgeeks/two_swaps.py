'''
Given a permutation of some of the first natural numbers in an array arr[], determine if the array can be sorted
in exactly two swaps. A swap can involve the same pair of indices twice.
Return true if it is possible to sort the array with exactly two swaps, otherwise return false.
'''
class Solution:
    def checkSorted(self, arr):
        n=2
        i=0
        end=len(arr)
        while i<end:
            if arr[i]!=(i+1):
                if n<1:
                    return False
                n-=1
                temp=arr[arr[i]-1]
                arr[arr[i]-1]=arr[i]
                arr[i]=temp
            else:
                i+=1
        if n==1:
            return False
        return True


arr = [4, 3, 2, 1]
print(Solution().checkSorted(arr))