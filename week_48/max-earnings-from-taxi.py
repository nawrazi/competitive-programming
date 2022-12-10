# https://leetcode.com/problems/maximum-earnings-from-taxi/description/

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        def findEarliest(time):
            left, right = 0, len(rides) - 1
            best = len(rides)
            
            while left <= right:
                mid = (left + right) // 2
                
                if rides[mid][0] >= time:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return best
        
        @cache
        def getProfit(point):
            if point >= len(rides):
                return 0
            
            next_point = findEarliest(rides[point][1])
            cur_profit = rides[point][2] + rides[point][1] - rides[point][0]
            return max(getProfit(point + 1), cur_profit + getProfit(next_point))
        
        rides.sort()
        return getProfit(0)
    
