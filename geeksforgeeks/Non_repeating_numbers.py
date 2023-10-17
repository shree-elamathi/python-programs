##N = 2
##nums=[1,1,2,2,3,4]
##class Solution:
##    def singleNumber(self, nums):
##        nums.sort()
##        print(nums)
##        x=len(nums)
##        for i in range(x-1):
##            if nums[i]==nums[i+1]:
##                a=nums[i]
##                b=nums[i+1]
##                print(a)
##                print(b)
##                nums.remove(a)
##                nums.remove(b)
##        
##ob=Solution()
##ob.singleNumber(nums)

##N=2
##nums=[1,1,2,2,3,4]
##class Solution:
##    def singleNumber(self,nums):
##        nums.sort()
##        x=len(nums)
##        if x==0:
##            print(nums)
##        elif nums[x-1]==nums[x-2]:
##            nums.remove(nums[x])
##            nums.remove(nums[x+1])
##            ob.singleNumber(nums)
##        else:
##            print(nums)
##
##ob=Solution()
##ob.singleNumber(nums)
            
N=2
nums=[1,2,3,2,4,1]
class Soution:
    def singleNumber(self,nums):
        nums.sort()
