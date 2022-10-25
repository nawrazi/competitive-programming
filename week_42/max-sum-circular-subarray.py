# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -inf
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, num + cur_sum)
            max_sum = max(max_sum, cur_sum)
            
        min_sum = inf
        cur_sum = 0
        for num in nums[1:-1]:
            cur_sum = min(num, num + cur_sum)
            min_sum = min(min_sum, cur_sum)
            
        return max(max_sum, sum(nums) - min_sum)
    
