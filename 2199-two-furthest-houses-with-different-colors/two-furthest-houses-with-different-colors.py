class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist=0
        dist=0
        for i in range(len(colors)-1):
            
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    dist=j-i
                    if dist>max_dist:
                        max_dist=dist
        return max_dist                


        