class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        current=0
        total=0
        for i in reversed(s):
            char=hash_map[i]
            if char<current:
                total=total-char
            else:
                total=total+char
            current=char
        return total            

        
        