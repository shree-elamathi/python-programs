'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise,
return false.
'''
class Solution:
    def threeConsecutiveOdds(self,arr):
        if len(arr)<3:
            return False
        i=0
        j=i+2
        while j<len(arr):
            temp_arr=arr[i:j+1]
            count=0
            for k in temp_arr:
                if k%2!=0:
                    count+=1
                else:
                    break
            if count==3:
                return True
            i+=1
            j+=1
        return False
arr=[1,2,34,3,4,5,7,23,12]
print(Solution().threeConsecutiveOdds(arr))
