# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        zeros = s.count('0')
        flips = min(s.count('1'), s.count('0'))
        
        for idx in range(len(s)):
            flips = min(flips, zeros + ones)
            if s[idx] == '1':
                ones += 1
            else:
                zeros -= 1
                
        return flips
    
