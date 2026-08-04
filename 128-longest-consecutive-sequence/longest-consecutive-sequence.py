class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        current=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]-1:
                current=current+1
            elif nums[i-1]==nums[i]:
                continue
            else:
                longest=max(longest,current)
                current=1
        return max(longest,current)                



        