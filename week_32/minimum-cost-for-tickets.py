# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        length = {0: 1, 1: 7, 2: 30}
        
        @cache
        def getCost(day):
            if day > days[-1]:
                return 0
            
            while day not in travel:
                day += 1
            
            min_cost = inf
            for i, cost in enumerate(costs):
                nex_cost = cost + getCost(day + length[i])
                min_cost = min(min_cost, nex_cost)
            
            return min_cost
        
        return getCost(1)
    
