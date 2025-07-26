class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map={}
        res=[]
        for i in nums:
            if i in hash_map:
                hash_map[i]=hash_map[i]+1
            else:
                hash_map[i]=1
        sorted_items = sorted(hash_map.items(), key=lambda x: (x[1], -x[0]))

       
        for key, value in sorted_items:
            res += [key] * value

        return res