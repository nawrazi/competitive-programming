# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        cur_min = inf
        max_diff = -1
        for num in nums:
            if num <= cur_min:
                cur_min = num
            else:
                max_diff = max(max_diff, num - cur_min)
                
        return max_diff
    
