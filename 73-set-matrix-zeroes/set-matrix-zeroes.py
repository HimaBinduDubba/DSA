class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_r=set()
        zero_c=set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    zero_r.add(i)
                    zero_c.add(j)
        for r in zero_r:
            for j in range(cols):
                 matrix[r][j]=0
        for c in zero_c:
            for i in range(rows):
                matrix[i][c]=0                   