# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        suffix = [0]
        for c in reversed(s):
            suffix.append(suffix[-1])
            if c == '0':
                suffix[-1] += 1
        
        suffix.reverse()
        suffix.pop()
        zeros = 0
        flips = min(s.count('1'), s.count('0'))
        
        for idx, ones in enumerate(suffix):
            flips = min(flips, zeros + ones)
            zeros += int(s[idx])
            
        return flips
    
