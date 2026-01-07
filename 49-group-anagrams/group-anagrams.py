class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs=[]
        for i in range(len(strs)):
            sorted_strs.append(tuple(sorted(strs[i])))
        map={}
        for i in range(len(strs)):
            if sorted_strs[i] in map:
                map[sorted_strs[i]].append(strs[i])
            else:
                map[sorted_strs[i]]=[strs[i]]
        res=[]
        for key in map:
            res.append(map[key])
        return res            

        