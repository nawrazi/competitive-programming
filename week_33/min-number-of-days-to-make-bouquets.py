# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def getBouqets(days):
            bouqets, cur = 0, 0
            for day in bloomDay:
                if day <= days:
                    cur += 1
                    if cur == k:
                        bouqets += 1
                        cur = 0
                else:
                    cur = 0
            return bouqets
        
        start, end = 1, max(bloomDay)
        best = -1
        
        while start <= end:
            mid = (start + end) // 2
            if getBouqets(mid) >= m:
                best = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return best
    
