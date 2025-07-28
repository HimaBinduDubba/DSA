class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        row=0
        i=1
        while count+i<=n:
            count=count+i
            row=row+1
            i=i+1
        return row    


        