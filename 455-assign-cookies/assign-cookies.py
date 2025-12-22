class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()      
        i=0
        j=0
        count=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count=count+1
                i=i+1
                
            j=j+1
        return count        



        