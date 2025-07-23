class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        tri=[[0]*(i+1) for i in range(n)]
        for i in range(n):
            tri[i][0]=1
            tri[i][i]=1
            for j in range(1,i):
                tri[i][j]=tri[i-1][j-1]+tri[i-1][j]
        return tri        
        