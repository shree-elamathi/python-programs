'''
Convert a non-negative integer num to its English words representation.
'''
class Solution:
    def numberToWords(self,num):
        if num==0:
            return "Zero"
        def numbertowordshelper(num):
            digitstr=["zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
            teenstr=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
            tenstr=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
            res=""
            if num>99:
                res+=digitstr[num//100]+ " Hundred "
            num%=100
            if num<20 and num>9:
                res+=teenstr[num-10]+" "
            else:
                if num>=20:
                    res+=tenstr[num//10]+" "
                num%=10
                if num>0:
                    res+=digitstr[num]+" "
            return res
        bigstr=["Thousand","Million","Billion"]
        res=numbertowordshelper(num%1000)
        num//=1000
        for i in range(len(bigstr)):
            if num>0 and num%1000>0:
                res =numbertowordshelper(num % 1000) + bigstr[i] + " " + res
            num//=1000
            return res.strip()

num=12345
print(Solution().numberToWords(num))
