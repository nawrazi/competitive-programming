# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix = [0]
        for c in s:
            prefix.append(prefix[-1])
            if c == '1':
                prefix[-1] += 1
        prefix.pop()
        
        suffix = [0]
        for c in reversed(s):
            suffix.append(suffix[-1])
            if c == '0':
                suffix[-1] += 1
        suffix.reverse()
        suffix.pop()
        
        flips = min(s.count('1'), s.count('0'))
        for zeros, ones in zip(prefix, suffix):
            flips = min(flips, zeros + ones)
            print(zeros + ones, flips)
            
        return flips
    
