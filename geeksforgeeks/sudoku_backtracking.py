if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1

class Solution:
    def SolveSudoku(self,grid):
        for i in range(9):
            for j in range(9):
                if(grid[i][j]==0):
                    for k in range(1,10):
                        if ob.issafe(grid,k):
                            grid[i][j]=k
                        return True
                    
    def issafe(self,grid,k):
        for i in range (9):
            for j in range(9):
                if grid[i][j]==k:
                    return True
                    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
            

