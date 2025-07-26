class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        i=0;j=0
        count=0
        while i<len(heights) and j<len(expected):
            if heights[i]!=expected[i]:
                count=count+1
                i=i+1
                j=j+1
            else:
                i=i+1
                j=j+1
        return count            

        