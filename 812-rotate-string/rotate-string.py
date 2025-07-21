class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        result=""    
        l1=list(s)                                                            
        for i in range(len(s)):
            result=''.join(l1[i+1:len(s)])+''.join(l1[0:i+1])
            if result==goal:
                return True
        return False        




        