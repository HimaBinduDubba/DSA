class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        pre_product=1
        post_product=1
        for i in range(1,len(nums)):
            pre_product=pre_product*nums[i-1]
            prefix[i]=pre_product
        for i in range(len(nums)-2,-1,-1):
            post_product=post_product*nums[i+1]
            postfix[i]=post_product
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=res[i]+(prefix[i]*postfix[i])      
        return res      






        