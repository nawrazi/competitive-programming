# https://leetcode.com/problems/maximum-subarray/
# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            best_sum = max(best_sum, cur_sum)

        return best_sum
    
