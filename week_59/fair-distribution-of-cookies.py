# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        buckets = [0 for _ in range(k)]
        self.unfairness = inf
        
        def distribute(idx):
            if idx >= len(cookies):
                self.unfairness = min(self.unfairness, max(buckets))
                return
            
            if max(buckets) >= self.unfairness:
                return
            
            for i in range(k):
                buckets[i] += cookies[idx]
                distribute(idx + 1)
                buckets[i] -= cookies[idx]
                
        distribute(0)
        return self.unfairness
    
