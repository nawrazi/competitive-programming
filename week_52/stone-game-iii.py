# https://leetcode.com/problems/stone-game-iii/description/

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def getScore(idx, alice):
            if idx >= len(stoneValue):
                return 0
            
            optimal = -inf if alice else inf
            stones = 0
            
            for i in range(idx, min(idx + 3, len(stoneValue))):
                score = getScore(i + 1, not alice)
                stones += stoneValue[i]
                if alice:
                    optimal = max(score + stones, optimal)
                else:
                    optimal = min(score - stones, optimal)
                    
            return optimal
        
        winner = getScore(0, True)
        
        if winner > 0:
            return 'Alice'
        elif winner < 0:
            return 'Bob'
        else:
            return 'Tie'
        
