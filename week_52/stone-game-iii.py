# https://leetcode.com/problems/stone-game-iii/description/

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def getScore(idx, alice):
            if idx >= len(stoneValue):
                return 0
            
            if alice:
                max_score = -inf
                stones = 0
                for i in range(idx, min(idx + 3, len(stoneValue))):
                    score = getScore(i + 1, False)
                    stones += stoneValue[i]
                    max_score = max(score + stones, max_score)
                    
                return max_score
            
            else:
                min_score = inf
                stones = 0
                for i in range(idx, min(idx + 3, len(stoneValue))):
                    score = getScore(i + 1, True)
                    stones += stoneValue[i]
                    min_score = min(score - stones, min_score)
                    
                return min_score
            
        winner = getScore(0, True)
        
        if winner > 0:
            return 'Alice'
        elif winner < 0:
            return 'Bob'
        else:
            return 'Tie'
        
