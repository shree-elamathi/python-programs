#there are n cities in a Geekland. Each city is given some beautifulness by the king. Cities wih
#different beautifulness don't lilke to trade with each other. You are given with q queries each consisting
#of two integers u and v. You need to tell if all the cities from u to v (both inclusive) can trade with
#each other city from u to v.
class Solution:
    def canTrade(self,n,b,q,qu):
        arr=[]
        for city in qu:
            val=b[city[0]-1]
            for i in range(city[0]-1,city[1]):
                if b[i]!=val:
                    arr.append(0)
                    break
            else:
                arr.append(1)
        return arr


n=6
b=[2,1,6,5,3,4]
q=4
qu=[[1,2],[2,5],[5,6],[6,6]]
print(Solution().canTrade(n,b,q,qu))