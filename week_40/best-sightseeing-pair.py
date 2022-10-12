# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = -inf
        ans = -inf
        for i, num in enumerate(values):
            ans = max(ans, best + num - i)
            best = max(best, num + i)
            
        return ans
    
