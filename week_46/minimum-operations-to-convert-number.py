# https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([(start, 0)])
        seen = set()
        
        while q:
            val, ops = q.popleft()
            
            if val == goal:
                return ops
            
            if not 0 <= val <= 1000 or val in seen:
                continue
            
            seen.add(val)
            for num in nums:
                q.append((val + num, ops + 1))
                q.append((val - num, ops + 1))
                q.append((val ^ num, ops + 1))
                
        return -1
    
