# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        i = 0
        while i < n - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals.pop(i + 1)
                n -= 1
                continue
            i += 1
        
        return intervals
    
