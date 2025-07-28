class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for num in nums:
            res.append(num**2)
        return sorted(res) 
        