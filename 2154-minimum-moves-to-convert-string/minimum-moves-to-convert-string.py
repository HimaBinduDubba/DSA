class Solution:
    def minimumMoves(self, s: str) -> int:
        i=0
        count=0
        while i<len(s):
            if s[i]=='X':
                count=count+1
                i=i+3
            else:
                i=i+1
        return count            


        