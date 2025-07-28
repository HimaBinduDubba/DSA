class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        sorted_nums=sorted(nums)
        for num in nums:
            res.append(sorted_nums.index(num))
        return res    