# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        starts = sorted([s for s, _ in flowers])
        ends = sorted([e for _, e in flowers])
        
        def startedBefore(time): # bisect_right
            start, end = 0, len(starts) - 1
            best = len(starts)
            while start <= end:
                mid = (start + end) // 2
                if time > starts[mid]:
                    start = mid + 1
                elif time < starts[mid]:
                    best = mid
                    end = mid - 1
                else:
                    best = mid + 1
                    start = mid + 1
            return best

        def endedBefore(time): # bisect_left
            start, end = 0, len(ends) - 1
            best = 0
            while start <= end:
                mid = (start + end) // 2
                if time > ends[mid]:
                    best = mid + 1
                    start = mid + 1
                elif time < ends[mid]:
                    end = mid - 1
                else:
                    best = mid
                    end = mid - 1
            return best
        
        return [startedBefore(t) - endedBefore(t) for t in persons]
    
