class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res=[]
        s=sentence.split()
        for idx,i in enumerate(s):
            res1=""
            if i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u' or i[0]=='A' or i[0]=='E' or i[0]=='I' or i[0]=='O' or i[0]=='U':
                res1=i+'ma'+'a'*(idx+1)
            else:
                res1=i[1:]+i[0]+'ma'+'a'*(idx+1)
            res.append(res1)    
        return ' '.join(res)        





        