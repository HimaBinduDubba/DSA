class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if nums.count(i)>1:
                res.append(i)
                break
        nums_set=set(nums)
        res_set=set(range(1,len(nums)+1))
        res.append(list(res_set-nums_set)[0]) 
        return res
        