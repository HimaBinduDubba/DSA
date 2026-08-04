class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        res=[]
        for num in nums:
            if num in map:
                map[num]=map[num]+1
            else:
                map[num]=1
        sorted_map=dict(sorted(map.items(),key=lambda x:x[1],reverse=True))
        return list(sorted_map.keys())[:k]