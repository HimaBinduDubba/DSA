class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        start=0
        mid=len(nums)//2
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1            



        