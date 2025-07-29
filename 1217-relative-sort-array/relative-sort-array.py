class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        res1=[]
        temp=arr1[:]
        for i in arr2:
            count=arr1.count(i)
            
            for _ in range(count):
                    res.append(i)
                    arr1.remove(i)
        temp=arr1[:]                
        for i in temp:
            count = arr1.count(i)
            for _ in range(count):
                res1.append(i)
                arr1.remove(i)    
        res1.sort()              
        return res+res1        



