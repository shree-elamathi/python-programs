'''
Merge sort has an time complexity of O(n log n)
'''
class Solution:
    def sortArray(self,nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        lefthalf=nums[:mid]
        righthalf=nums[mid:]
        sortedleft=self.sortArray(lefthalf)
        sortedright=self.sortArray(righthalf)
        return self.merge(sortedleft,sortedright)

    def merge(self,left,right):
        result=[]
        i=j=0
        while i <len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

nums = [5,2,3,1]
print(Solution().sortArray(nums))