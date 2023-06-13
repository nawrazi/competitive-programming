# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def count(pos, moves):
            if moves == steps:
                return pos == 0
            
            left = count(pos - 1, moves + 1) if pos > 0 else 0
            right = count(pos + 1, moves + 1) if pos < arrLen - 1 else 0
            stay = count(pos, moves + 1)
            
            return (left + right + stay) % mod
        
        mod = pow(10, 9) + 7
        return count(0, 0)
    
