class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map={}
        res=""
        for i in s:
            if i in hash_map:
                hash_map[i]=hash_map[i]+1
            else:
                hash_map[i]=1
        sorted_hash = dict(sorted(hash_map.items(), key=lambda x: (x[1], x[0]), reverse=True))

        for key,value in sorted_hash.items():
            
                res=res+key*value
        return res        


        