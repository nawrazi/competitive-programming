# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda d: (d[0], -d[1]))
        dp = []
        
        def bisect(num):
            start, end = 0, len(dp) - 1
            best = 0
            
            while start <= end:
                mid = (start + end) // 2
                
                if num > dp[mid]:
                    best = mid + 1
                    start = mid + 1
                elif num < dp[mid]:
                    end = mid - 1
                else:
                    best = mid
                    end = mid - 1
                    
            return best
        
        for _, h in envelopes:
            pos = bisect(h)
            
            if pos == len(dp):
                dp.append(h)
            else:
                dp[pos] = h
                
        return len(dp)
    
