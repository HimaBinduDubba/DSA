class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))
        hashmap={}
        for i in range(len(arr_sorted)):
            hashmap[arr_sorted[i]]=i+1
        res = []
        for i in arr:
            res.append(hashmap[i])
        return res