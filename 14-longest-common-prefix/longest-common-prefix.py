class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strs=sorted(strs)
        i=0
        j=0
        while i<len(strs[0]) and j<len(strs[-1]):
            if strs[0][i]!=strs[-1][j]:
                return strs[0][0:i]
            i=i+1
            j=j+1
        return strs[0][0:i]            

        