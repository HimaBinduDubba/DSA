class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        res=[]
        for word in s_list:
            
            res.append(word[::-1])
        return " ".join(res)    

        