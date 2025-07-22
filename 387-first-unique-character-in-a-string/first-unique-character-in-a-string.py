class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        for key,value in freq.items():
            if value==1:
                return s.index(key)
        return -1                    
        