# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        min_flips = s.count('1')
        flips = s.count('0')
        
        for idx in range(len(s)):
            min_flips = min(min_flips, flips)
            flips += 1 if s[idx] == '1' else -1
            
        return min_flips
    
