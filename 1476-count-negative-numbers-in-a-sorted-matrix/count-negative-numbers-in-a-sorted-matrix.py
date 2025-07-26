class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for num in grid:

            for j in num:
                if j<0:
                    count=count+1
        return count            
        