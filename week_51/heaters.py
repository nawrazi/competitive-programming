# https://leetcode.com/problems/heaters/description/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def canCover(radius):
            ranges = [[heater - radius, heater + radius] for heater in heaters]
            cur = 0
            
            for house in houses:
                while cur < len(ranges) and (house < ranges[cur][0] or house > ranges[cur][1]):
                    cur += 1
                    
                if cur >= len(ranges) or house < ranges[cur][0] or house > ranges[cur][1]:
                    return False
                
            return True
        
        houses.sort()
        heaters.sort()
        left, right = 0, pow(10, 9)
        best = right
        
        while left <= right:
            mid = (left + right) // 2
            if canCover(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
    
