# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(pos):
            if pos >= len(cost) - 2:
                return cost[pos]

            min_step = float(inf)
            for move in [pos+1, pos+2]:
                if move in mem:
                    step = mem[move]
                else:
                    step = climb(move)
                    mem[move] = step

                min_step = min(min_step, step)

            return cost[pos] + min_step

        mem = {}
        return min(climb(0), climb(1))
