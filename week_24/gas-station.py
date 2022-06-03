# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_tank, whole_tank = 0, 0
        cur_start = 0
        
        for i in range(len(gas)):
            cur_cost = gas[i] - cost[i]
            cur_tank += cur_cost
            whole_tank += cur_cost
            
            if cur_tank < 0:
                cur_tank = 0
                cur_start = i + 1
                
        return cur_start if whole_tank >= 0 else -1
    
