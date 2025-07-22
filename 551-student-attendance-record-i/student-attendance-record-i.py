class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        for i in s:
            if i=='A':
                count=count+1
            if count>1:
                return False
        for i in range(len(s)-2):
            if s[i:i+3]=='LLL':
                return False
        return True                    
        