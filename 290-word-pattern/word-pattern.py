class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split(" ")
        return [pattern.index(c) for c in pattern]==[s.index(c) for c in s]


        