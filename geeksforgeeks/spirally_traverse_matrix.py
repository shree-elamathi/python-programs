'''
You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.
'''
class Solution:
    def spirallyTraverse(self, matrix):
        def boundaryTraversal( matrix, startr,startc,endr,endc):
            a = []
            for col in range(startc,endc+1):
                a.append(matrix[startr][col])
            for row in range(startr+1,endr+1):
                a.append(matrix[row][endc])
            if startr < endr:
                for col in range(endc - 1, startc - 1, -1):
                    a.append(matrix[endr][col])
            if startc < endc:
                for row in range(endr - 1, startr, -1):
                    a.append(matrix[row][startc])
            return a

        if not matrix or not matrix[0]:
            return []
        res=[]
        startr,startc=0,0
        endr,endc=len(matrix)-1,len(matrix[0])-1
        while startr<=endr and startc<=endc:
            res.extend(boundaryTraversal(matrix,startr,startc,endr,endc))
            startr+=1
            endr-=1
            startc+=1
            endc-=1
        return res

matrix= [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spirallyTraverse(matrix))