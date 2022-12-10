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
        def getValue(event, first):
            if event >= len(events):
                return 0
            
            next_event = findEarliest(events[event][1])
            if first:
                return max(events[event][2] + getValue(next_event, False), getValue(event + 1, True))
            else:
                return max(getValue(event + 1, False), events[event][2])
            
        events.sort()
        return getValue(0, True)
    
