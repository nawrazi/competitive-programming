# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        current = []
        
        def form(idx):
            if idx >= len(s):
                return len(current) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if len(current) >= 1 and val != current[-1] - 1:
                    continue
                
                if len(current) < 2 or val == current[-1] - 1:
                    current.append(val)
                    if form(i + 1):
                        return True
                    current.pop()
                    
        return form(0)
    
