class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.add((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif total<0:
                    left=left+1
                else:
                    right=right-1        
        return list(res)  