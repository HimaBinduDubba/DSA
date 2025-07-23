class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int=int(a,2)
        b_int=int(b,2)
        res_int=a_int+b_int
        res=bin(res_int)
        return res[2:]

        