class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        res1=[]
        res2=[]
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        res1.sort()
        res2.sort(reverse=True)
        i=0;j=0
        while i<len(res1) and j<len(res2):
            result.append(res1[i])
            
            result.append(res2[j])
           
            i=i+1
            j=j+1
        if i<len(res1):
            result.append(res1[i])       
        return result    


        