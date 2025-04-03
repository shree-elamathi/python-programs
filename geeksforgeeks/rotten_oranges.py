'''
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the
following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges
We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index
(i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a
unit time.
Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.
'''

from collections import deque
class Solution:
    def orangesRotting(self, mat):
        r,c=len(mat),len(mat[0])
        v=[[1 for i in range(c)] for j in range(r)]
        q=deque()
        ans=0
        for i in range(r):
            for j in range(c):
                if mat[i][j]==2:
                    q.append([i,j])
                    v[i][j]=0
        q.append(-1)
        while q:
            ele=q.popleft()
            if ele==-1:
                if q:
                    q.append(-1)
                else:
                    break
                ans += 1
                continue
            m,n=ele[0],ele[1]
            if (m+1)<r and v[m+1][n] and mat[m+1][n]==1:
                v[m+1][n]=0
                q.append([m+1,n])
            if (m-1)>=0 and v[m-1][n] and mat[m-1][n]==1:
                v[m-1][n]=0
                q.append([m-1,n])
            if (n+1)<c and v[m][n+1] and mat[m][n+1]==1:
                v[m][n+1]=0
                q.append([m,n+1])
            if (n-1)>=0 and v[m][n-1] and mat[m][n-1]==1:
                v[m][n-1]=0
                q.append([m,n-1])
        for i in range(r):
            for j in range(c):
                if v[i][j]==mat[i][j]:
                    return -1
        return ans

mat = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
print(Solution().orangesRotting(mat))
