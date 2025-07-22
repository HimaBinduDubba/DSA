class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        current_sum=0
        prev_sum=0
        for i in reversed(s):
            char=mapping[i]
            if char<prev_sum:
                current_sum=current_sum-char
            else:
                current_sum=current_sum+char
            prev_sum=char
        return current_sum        


        