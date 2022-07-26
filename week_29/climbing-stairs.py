# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(step):
            if step >= n - 1:
                return 1
            
            if step + 1 not in cache:
                cache[step + 1] = climb(step + 1)
                
            if step + 2 not in cache:
                cache[step + 2] = climb(step + 2)
            
            return cache[step + 1] + cache[step + 2]
        
        cache = {}
        return climb(0)
    
