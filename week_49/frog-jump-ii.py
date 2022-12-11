# https://leetcode.com/problems/frog-jump-ii/description/

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]
        
        max_forward, max_backward = 0, 0
        for i in range(2, len(stones), 2):
            max_forward = max(stones[i] - stones[i - 2], max_forward)
            
        for i in range(3, len(stones), 2):
            max_backward = max(stones[i] - stones[i - 2], max_backward)
            
        return max(max_forward, max_backward)
    
