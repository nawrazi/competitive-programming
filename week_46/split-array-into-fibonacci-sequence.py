# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        current = []
        
        def form(idx):
            if idx >= len(num):
                return len(current) >= 3
            
            for i in range(idx, len(num)):
                val = int(num[idx:i+1])
                if val >= pow(2, 31):
                    return False
                
                if len(current) < 2 or val == current[-1] + current[-2]:
                    current.append(val)
                    if form(i + 1):
                        return True
                    current.pop()
                    
                if num[idx] == '0':
                    return False
                
        form(0)
        return current
    
