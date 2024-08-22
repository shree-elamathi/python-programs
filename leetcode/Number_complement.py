'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its
binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
'''
class Solution:
    def findComplement(self,num):
        str=bin(num)[2:]
        arr=[]
        for i in str:
            if i == "0":
                arr.append("1")
            else:
                arr.append("0")
        str1=int("".join(arr),2)
        return str1
num=5
print(Solution().findComplement(num))