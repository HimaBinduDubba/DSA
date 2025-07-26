class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        count=int(n*(0.05))
        arr=arr[count:n-count]
        return sum(arr)/len(arr)
