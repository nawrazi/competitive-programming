# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        i=0
        while i<n-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i]=[intervals[i][0], max(intervals[i+1][1],intervals[i][1])]
                intervals.pop(i+1)
                n-=1
                continue
            i+=1

        return intervals
