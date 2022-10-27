# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def getLongest(idx, last, increase):
            if idx >= len(nums):
                return 0
            
            longest = getLongest(idx + 1, last, increase)
            if increase and nums[idx] > last:
                longest = max(longest, 1 + getLongest(idx + 1, nums[idx], False))
            elif not increase and nums[idx] < last:
                longest = max(longest, 1 + getLongest(idx + 1, nums[idx], True))
                
            return longest
        
        return max(getLongest(0, -inf, True), getLongest(0, inf, False))
    
