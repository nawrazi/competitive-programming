# https://leetcode.com/problems/beautiful-arrangement/description/

class Solution:
    def countArrangement(self, n: int) -> int:
        def count(idx, mask):
            if idx > n:
                return 1
            
            arrangements = 0
            for num in range(1, n + 1):
                if mask & 1 << num == 0 and (idx % num == 0 or num % idx == 0):
                    arrangements += count(idx + 1, mask | 1 << num)
                    
            return arrangements
        
        return count(1, 0)
    
