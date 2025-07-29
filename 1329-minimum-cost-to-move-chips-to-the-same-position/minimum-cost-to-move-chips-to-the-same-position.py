class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even=0;odd=0
        for i in position:
            if i%2==0:
                even=even+1
            else:
                odd=odd+1
        return min(even,odd)            

