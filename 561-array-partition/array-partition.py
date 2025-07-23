class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum=0
        for i in range(0,len(nums),2):
           min_sum=min_sum+nums[i]
        return min_sum    
        