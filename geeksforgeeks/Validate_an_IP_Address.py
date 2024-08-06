'''
You are given a string str in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid
return true otherwise return false.
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each
ranging from 0 to 255, separated by dots, e.g., 172.16.254.1
A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized
form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)
Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.
'''
class Solution:
    def isValid(self, str):
        arr = str.split(".")
        if str[0] == "." or str[len(str) - 1] == ".":
            return False
        if len(arr) != 4 or "" in arr:
            return False
        for i in arr:
            if len(i) > 1 and i[0] == "0":
                return False
            try:
                if 0 <= int(i) <= 255:
                    continue
                else:
                    return False
            except:
                return False
        return True
str="192.168.1.1.."
print(Solution().isValid(str))
