
class Solution(object):
    def setZeroes(self, matrix):
        s=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    s.append((i,j))
        for i,j in s:
            for k in range(len(matrix[i])):
                matrix[i][k]=0
            for k in range(len(matrix)):
                matrix[k][j]=0
        return matrix                        