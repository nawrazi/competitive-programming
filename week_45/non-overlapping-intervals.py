# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        last = -inf
        clean = 0
        for start, end in sorted(intervals, key = lambda i: i[1]):
            if start >= last:
                last = end
                clean += 1
                
        return len(intervals) - clean
    
