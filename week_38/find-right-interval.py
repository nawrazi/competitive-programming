# https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[s, e, i] for i, (s, e) in enumerate(intervals)]
        intervals.sort()
        
        def search(target):
            start, end = 0, len(intervals) - 1
            best = -1
            
            while start <= end:
                mid = (start + end) // 2
                
                if intervals[mid][0] >= target:
                    best = intervals[mid][2]
                    end = mid - 1
                else:
                    start = mid + 1
                    
            return best
            
        right = [0 for _ in range(len(intervals))]
        for _, end, index in intervals:
            right[index] = search(end)
            
        return right
    
