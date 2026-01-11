class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if goal==s:
            return True
        
        for i in range(1,len(s)):
            if s[i:len(s)]+s[0:i]==goal:
                return True
        return False        
        