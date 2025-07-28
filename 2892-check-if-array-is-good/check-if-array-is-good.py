class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        if max(nums)!=n-1:
            return False
        for i in range(1,n-1):
            if nums.count(i)!=1:
                return False
        if nums.count(max(nums))!=2:
            return False
        return True                





        