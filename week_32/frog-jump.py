# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        safe = set(stones)
        target = stones[-1]
        
        @cache
        def reach(pos, jump):
            if pos == target:
                return True
            
            for nex in [-1, 0, 1]:
                nex_jump = jump + nex
                nex_pos = pos + nex_jump
                if nex_pos in safe and nex_jump > 0:
                    if reach(nex_pos, nex_jump):
                        return True
                    
            return False
        
        return reach(0, 0)
    
