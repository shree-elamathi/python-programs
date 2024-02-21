# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers
# in this range, inclusive.
class solution:
    def rangebitwiseand(self, left, right):
        if left==1 and right==1:
            return 1
        if left<=1 and right==1:
            return 0
        val=left
        for i in range(left+1,right+1):
                val=val&i
        return val
#another method
#time complexity solved
#while right>left:
#right = right&(right-1)
#return right&left

left=5
right=7
print(solution().rangebitwiseand(left,right))
