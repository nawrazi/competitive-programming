# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def canReach(speed):
            time = 0
            for i, d in enumerate(dist):
                time += ceil(d / speed) if i < len(dist) - 1 else d / speed
            return time <= hour
        
        start, end = 1, pow(10, 9)
        best = -1
        
        while start <= end:
            mid = (start + end) // 2
            if canReach(mid):
                best = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return best
    
