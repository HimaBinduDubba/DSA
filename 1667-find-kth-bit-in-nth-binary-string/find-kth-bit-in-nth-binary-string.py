class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s:str):
            s_list=list(s)
            return ''.join('1' if c=='0' else '0' for c in s)
        s1='0'    
        for _ in range(n+1):
            s1=s1+"1"+invert(s1)[::-1]
        return s1[k-1]    



        