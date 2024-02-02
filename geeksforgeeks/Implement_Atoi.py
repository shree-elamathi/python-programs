#Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions.
# If the conversion is not feasible, the function should return -1.
# Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-'
# and rest are numeric.

class solution:
    def atoi(self,s):
        num = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
        if s[0]=='-':
            for i in range(1,len(s)):
                if s[i] not in num:
                    return -1
        else:
            for i in range(0,len(s)):
                if s[i] not in num:
                    return -1
        return int(s)
s='-665'
print(solution().atoi(s))