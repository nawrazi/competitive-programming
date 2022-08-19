# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTimeToEat(pace):
            time = 0
            for pile in piles:
                time += pile // pace
                if pile % pace != 0:
                    time += 1
            return time
        
        start, end = 1, max(piles)
        best = -1
        while start <= end:
            mid = (start + end) // 2
            if getTimeToEat(mid) <= h:
                best = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return best
    
