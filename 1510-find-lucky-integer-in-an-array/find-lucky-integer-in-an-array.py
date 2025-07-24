class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        largest=-1
        for i in arr:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        for key,values in freq.items():
            
            if key==values and key>largest:
                largest=key
            
        return largest                    