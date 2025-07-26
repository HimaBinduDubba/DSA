class Solution:
    def sortSentence(self, s: str) -> str:
        hash_map={}
        res=[""]*len(s)
        result=""
        s=s.split()
        for i in s:
            hash_map[i]=int(i[-1])
        for key,value in hash_map.items():
            res[value-1]=key[:-1]
        for i in res:
            result=result+i+" "
           
        return result.strip()             





        