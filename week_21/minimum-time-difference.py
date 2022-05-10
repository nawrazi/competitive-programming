# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hour, minute = time.split(':')
            cur_time = (int(hour) * 60) + int(minute)
            times.append(cur_time)
            
        times.sort()
        min_diff = float(inf)
        for i in range(1, len(times)):
            diff = min(times[i] - times[i-1], 1440 - times[i] + times[i-1])
            min_diff = min(diff, min_diff)
            
        return min(min_diff, 1440 - times[-1] + times[0])
