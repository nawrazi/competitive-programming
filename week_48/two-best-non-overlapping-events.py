# https://leetcode.com/problems/two-best-non-overlapping-events/description/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def findEarliest(time):
            left, right = 0, len(events) - 1
            best = len(events)
            
            while left <= right:
                mid = (left + right) // 2
                
                if events[mid][0] > time:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return best
        
        @cache
        def getProfit(event, first):
            if event >= len(events):
                return 0
            
            next_event = findEarliest(events[event][1])
            if first:
                return max(events[event][2] + getProfit(next_event, False), getProfit(event + 1, True))
            else:
                return max(getProfit(event + 1, False), events[event][2])
            
        events.sort()
        return getProfit(0, True)
    
