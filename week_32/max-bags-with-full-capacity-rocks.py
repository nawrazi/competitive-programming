# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        spaces = [capacity[i] - rocks[i] for i in range(len(rocks))]
        spaces.sort(reverse=True)
        
        fullBags = 0
        while spaces and additionalRocks >= spaces[-1]:
            additionalRocks -= spaces.pop()
            fullBags += 1
            
        return fullBags
    
