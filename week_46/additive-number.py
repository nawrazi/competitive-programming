# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        current = []
        
        def form(idx):
            if idx >= len(num):
                return len(current) >= 3
            
            for i in range(idx, len(num)):
                val = int(num[idx:i+1])
                if len(current) < 2 or val == current[-1] + current[-2]:
                    current.append(val)
                    if form(i + 1):
                        return True
                    current.pop()
                    
                if num[idx] == '0':
                    return False
                    
        return form(0)
    
