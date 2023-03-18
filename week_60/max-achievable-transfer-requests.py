# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        bldgs = [0 for _ in range(n)]
        self.max_grants = 0
        
        def backtrack(idx, grants):
            if idx >= len(requests):
                if not any(bldgs):
                    self.max_grants = max(self.max_grants, grants)
                return
            
            backtrack(idx + 1, grants)
            
            bldgs[requests[idx][0]] -= 1
            bldgs[requests[idx][1]] += 1
            backtrack(idx + 1, grants + 1)
            bldgs[requests[idx][0]] += 1
            bldgs[requests[idx][1]] -= 1
            
        backtrack(0, 0)
        return self.max_grants
    
