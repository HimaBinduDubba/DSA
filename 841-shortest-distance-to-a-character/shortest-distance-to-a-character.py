class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res=[0]*len(s)
        res1=[]
        for i in range(len(s)):
            if s[i]==c:
                res1.append(i)
        for j in range(len(s)):
            min_dist=float('inf')
            for idx in res1:
                min_dist=min(min_dist,abs(j-idx))
            res[j]=min_dist
        return res        


                
