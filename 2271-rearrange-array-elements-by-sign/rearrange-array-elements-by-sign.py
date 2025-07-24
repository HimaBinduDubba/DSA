class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res1=[]
        res2=[]
        result=[]
        for i in nums:
            if i>0:
                res1.append(i)
            else:
                res2.append(i)
        i=0;j=0
        while i<len(res1) and j<len(res2):
            result.append(res1[i])
            result.append(res2[j])
            i=i+1
            j=j+1
        return result    

        