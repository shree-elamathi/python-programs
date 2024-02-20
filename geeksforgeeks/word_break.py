#Given a string s and a dictionary of n words dictionary, find out if a s can be segmented into
# a space-separated sequence of dictionary words. Return 1 if it is possible to break the s into a
# sequence of dictionary words, else return 0.
# Note: From the dictionary dictionary each word can be taken any number of times and in any order.
class solution:
    def wordbreak(self,s,n,dictionary):
        val=[]
        ans=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    val.append(s[i:j+1])
        temp=""
        ans=0
        for i in val:
            temp+=i
        if len(temp)<len(s):
            return 0
        if temp==s:
            return 1
        i=0
        j=0
        ans=""
        while i<len(s) and j<len(temp):
            if s[i]==temp[j]:
                ans+=temp[j]
                i+=1
                j+=1
            else:
                j+=1
        if ans==s:
            return 1
        return 0





s="uvunewizkpoermegzkpoermegjvuiuvuijvunewizkpoermegsxygjsgsmivvshjsbhdptnewiisgsmigubitn"
n=9
dictionary=["newi","bhdpt","i","zkpoermeg","vvshjs","jvu","uvu","sgsmi","sxygj"]

print(solution().wordbreak(s,n,dictionary))