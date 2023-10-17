s="ABC"
class Solution:
    def permutation(self,s):
        from itertools import permutations
        a=permutations(s)
        result=sorted([''.join(p) for p in a])
        return result
            
ob=Solution()
ob.permutation(s)
            
        
