class Solution:
    def myAtoi(self, s: str) -> int:
        
        s=s.strip()
        if not s:
            return 0
        sign=1
        i=0
        res=0
        
        if s[i]=='-':
            sign=-1
            i=i+1
        elif s[i]=='+':
            i=i+1
        while i<len(s) and ord(s[i])>=48 and ord(s[i])<=57:
            res=res*10+(ord(s[i])-48)
            i=i+1
        res=sign*res  
        res = max(-2**31, min(res, 2**31 - 1))  
        return res    



        
       
        