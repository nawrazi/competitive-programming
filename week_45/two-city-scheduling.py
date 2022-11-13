# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key = lambda x: x[0] - x[1])
        
        total = 0
        for a, _ in costs[:n]:
            total += a
            
        for _, b in costs[n:]:
            total += b
            
        return total
    
