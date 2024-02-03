#You are given an array of n strings, which consists of lowercase English alphabets only, and an integer k.
# Find the number of valid strings in arr. A string is called as valid if it contains exactly k vowels.
class Solution:
    def valid_strins(self,n,k,arr):
        vow=["a","e","i","o","u"]
        count=0
        for word in arr:
            ans=[]
            for i in word:
                if i in vow:
                    ans.append(i)
            if len(ans)==k:
                count=count+1
        return count

n=4
k=2
arr=["aei","ae"]
print(Solution().valid_strins(n,k,arr))
