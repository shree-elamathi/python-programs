'''
Given a sentence containing several words and numbers. Find the largest number among them which does not
contain 9. If no such number exists, return -1.
Note: Numbers and words are separated by spaces only. It is guaranteed that there are no leading zeroes in the
answer.
'''
class Solution:
    def ExtractNumber(self,sentence):
        num=["1","2","3","4","5","6","7","8","9"]
        values=[]
        i=0
        while i<len(sentence):
            if sentence[i] in num:
                val=""
                while i<len(sentence) and sentence[i]!=" ":
                    val+=sentence[i]
                    i+=1
                if Solution().checkNum(val):
                    values.append(int(val))
            else:
                i+=1
        if len(values) != 0:
            return max(values)
        else:
            return "-1"

    def checkNum(self,val):
        for i in val:
            if i=="9":
                return False
        return True
sentence="zg 9 e 12 b 16 10 8 10 l 7"
print(Solution().ExtractNumber(sentence))