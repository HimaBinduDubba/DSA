class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        major=None
        for num in nums:
            if count==0:
                major=num
            if major==num:
                count=count+1
            else:
                count=count-1    
        return major        

        