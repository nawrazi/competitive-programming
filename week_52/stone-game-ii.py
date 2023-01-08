# https://leetcode.com/problems/stone-game-ii/description/

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def getStones(idx, alice, m):
            if idx >= len(piles):
                return 0
            
            if alice:
                max_stones = 0
                collected = 0
                for x in range(idx, min(idx + (m * 2), len(piles))):
                    stones = getStones(x + 1, False, max(m, x - idx + 1))
                    collected += piles[x]
                    max_stones = max(stones + collected, max_stones)
                    
                return max_stones
            
            else:
                min_stones = inf
                for x in range(idx, min(idx + (m * 2), len(piles))):
                    stones = getStones(x + 1, True, max(m, x - idx + 1))
                    min_stones = min(stones, min_stones)
                    
                return min_stones
            
        return getStones(0, True, 1)
    
