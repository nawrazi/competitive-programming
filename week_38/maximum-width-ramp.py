# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        pairs = [(n, i) for i, n in enumerate(nums)]
        max_ramp = 0
        min_idx = inf
        for _, idx in sorted(pairs):
            max_ramp = max(max_ramp, idx - min_idx)
            min_idx = min(min_idx, idx)
            
        return max_ramp
    
