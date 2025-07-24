class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        total=sum(nums)//3
        if sum(nums)%3!=0:
            return False
        pair=0
        current_sum=0
        for i in range(len(nums)):
            current_sum=current_sum+nums[i]
            if current_sum==total:
                pair=pair+1
                current_sum=0
        return pair>=3        
