'''
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system.
mapping[i] = j means digit i should be mapped to digit j in this system.
The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer
with mapping[i] for all 0 <= i <= 9.
You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the
mapped values of its elements.
Notes:
Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''
class Solution:
    def sortJumbled(self,mapping,nums):
        mapped={}
        val=[]
        for num in nums:
            map_val=""
            for each in str(num):
                map_val+=str(mapping[int(each)])
            mapped.update({map_val:num})
            val.append(map_val)
        val.sort(key=int)
        ans=[]
        for i in val:
            x=mapped[i]
            ans.append(x)
        return ans

mapping=[8,9,4,0,2,1,3,5,7,6]
nums=[991,338,38]
print(Solution().sortJumbled(mapping,nums))
