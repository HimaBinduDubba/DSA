class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        idx=-1
        for i in range(n-2,-1,-1):
            if nums[i+1]>nums[i]:
                idx=i
                break
        if idx!=-1:
            for j in range(n-1,-1,-1):
                if nums[j]>nums[idx]:
                    nums[j],nums[idx]=nums[idx],nums[j]
                    break
        nums[idx+1:]=reversed(nums[idx+1:])            


