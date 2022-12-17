# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        result = -inf
        
        for num in nums:
            prev_max = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * prev_max, num * cur_min)
            result = max(result, cur_max, cur_min)
            
        return result
    
