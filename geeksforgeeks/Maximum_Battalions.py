#Geek has the names of N soldiers represented as "names". He wants to divide them into battalions without changing the
# order of the names. The general will validate the division only if every soldier who has the same name belongs to the
#same battalion. Return the maximum number of battalions Geek could make.
class Solution:
    def maxbattalions(self,N,names):
        i=0
        j=N-1
        count=0
        while i<N and j>-1:
            if j!=i:
                if names[i]==names[j]:
                    count=count+1
                    i=j+1
                    j=N-1
                    temp=j
                else:
                    j=j-1
            else:
                i=i+1
                j=N-1
        if temp<N:
            count=count+1
        return count
N=47
names=["hbq","tkm","azi","xvu","hbq","hbq","glh","hbq","kxn","gst","zsl","xnl","gst","gst","glh","zrg","ccj",'qyz',
       'jem','jem','qyz','wzx','jfg','sey','jfg','ykh','cub','hbq','dot','ddm','sjm','ygr','zdn','bmk','kdk','xnl',
       'rkv','hbq','zmt','joi','tqe','ule','bmk','mhg','ccj','zdn','jkr']
print(Solution().maxbattalions(N,names))