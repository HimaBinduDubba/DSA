class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        res=""
        for i in range(len(s)-1):
            res=s[i+1:]+s[0:i+1]
            if res==goal:
                return True
        return False        

