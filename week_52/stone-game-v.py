# https://leetcode.com/problems/stone-game-v/description/

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0] + list(accumulate(stoneValue))
        
        @cache
        def getScore(start, end):
            if start == end:
                return 0
            
            if start == end - 1:
                return min(stoneValue[start], stoneValue[end])
            
            max_score = 0
            for idx in range(start, end):
                left_sum = prefix[idx + 1] - prefix[start]
                right_sum = prefix[end + 1] - prefix[idx + 1]
                
                if left_sum <= right_sum and 2 * left_sum > max_score:
                    max_score = max(max_score, left_sum + getScore(start, idx))
                    
                if left_sum >= right_sum and 2 * right_sum > max_score:
                    max_score = max(max_score, right_sum + getScore(idx + 1, end))
                    
            return max_score
        
        return getScore(0, len(stoneValue) - 1)
    
