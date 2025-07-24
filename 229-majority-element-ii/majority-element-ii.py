class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target=len(nums)//3
        freq={}
        res=[]
        for i in nums:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        for key,value in freq.items():
            if value>target:
                res.append(key)
        return res        





        