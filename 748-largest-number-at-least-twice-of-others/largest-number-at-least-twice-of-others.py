class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum=max(nums)
        temp=nums[:]
        nums.remove(maximum)
        for i in nums:
            if 2*i>maximum:
                return -1
        return temp.index(maximum)        

        