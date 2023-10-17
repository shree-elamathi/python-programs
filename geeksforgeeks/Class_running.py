class Solution:
    def common_element(self,v1,v2):
        v3=[]
        for i in range(0,n):
            for j in range(0,m):
                if v1[i]==v2[j]:
                    temp=v1[i]
                    v3.append(temp)
                    break
        v3.sort()
        return v3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):

        n=int(input())
        v1=list(map(int,input().split()))
        m=int(input())
        v2=list(map(int,input().split()))
        ob=Solution()
        ans=ob.common_element(v1,v2);
        for i in ans:
            print(i,end=" ")
        print()
