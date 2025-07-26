class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        end=float('-inf')
        for interval in intervals:
            start,finish=interval
            if start<end:
                count=count+1
            else:
                end=finish
        return count            
        
        