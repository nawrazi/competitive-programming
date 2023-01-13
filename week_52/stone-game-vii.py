# https://leetcode.com/problems/stone-game-vii/description/

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones, initial=0))
        
        @cache
        def getScore(left, right):
            if left == right:
                return 0
            
            pick_left = (prefix[right + 1] - prefix[left + 1]) - getScore(left + 1, right)
            pick_right = (prefix[right] - prefix[left]) - getScore(left, right - 1)
            
            return max(pick_left, pick_right)
        
        score = getScore(0, len(stones) - 1)
        getScore.cache_clear()
        return score
    
