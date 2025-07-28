class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=0
        i=1
        res=0
        while count!=k:
            if i not in arr:
                count=count+1
                res=i
            i=i+1
        return res        