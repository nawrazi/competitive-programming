# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def canPair(max_diff):
            pairs, i = 0, 0
            while i < len(nums):
                if abs(nums[i] - nums[i - 1]) <= max_diff:
                    pairs += 1
                    i += 2
                else:
                    i += 1
            return pairs >= p
        
        nums.sort()
        left, right = 0, max(nums) - min(nums)
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if canPair(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
    
