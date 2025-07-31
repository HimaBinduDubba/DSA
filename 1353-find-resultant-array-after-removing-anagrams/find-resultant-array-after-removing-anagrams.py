class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
       res=[] 
       prev=""
       for i in range(len(words)):
        if sorted(words[i])!=sorted(prev):
            res.append(words[i])
            prev=words[i]
       return res       

