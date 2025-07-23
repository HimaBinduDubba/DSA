class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set=set(nums)
        res_set=set(range(1,len(nums)+1))
        return list(res_set-nums_set)



        