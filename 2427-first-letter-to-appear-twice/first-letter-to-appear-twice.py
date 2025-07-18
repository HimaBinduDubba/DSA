class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]=freq[ch]+1
                if freq[ch]==2:
                    return ch
            else:
                freq[ch]=1
        return None        
              
        
        