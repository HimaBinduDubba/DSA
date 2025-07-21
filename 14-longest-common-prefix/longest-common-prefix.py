class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length=float('inf')
        prefix=""
        
        for word in strs:
            if len(word)<min_length:
                min_length=len(word)
        for i in range(min_length):
            current=strs[0][i]
            for word in strs:
                if word[i]!=current:
                    return prefix
            prefix=prefix+current 
        return prefix        
