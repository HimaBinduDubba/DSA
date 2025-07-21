class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1=set("QWERTYUIOP")
        row_2=set("ASDFGHJKL")
        row_3=set("ZXCVBNM")
        res=[]
        for word in words:
            if set(word.upper()).issubset(row_1) or set(word.upper()).issubset(row_2) or set(word.upper()).issubset(row_3):
                res.append(word)
        return res        
            


        