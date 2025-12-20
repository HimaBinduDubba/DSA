class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left=left+1
                        right=right-1
                    elif total<target:
                        left=left+1
                    else:
                        right=right-1
        return list(res)                





        
        