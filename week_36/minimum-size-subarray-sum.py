# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.append(0)
        cur_sum = 0
        min_length = inf
        l, r = 0, 0
        
        while l <= r < len(nums):
            if cur_sum < target:
                cur_sum += nums[r]
                r += 1
            else:
                min_length = min(min_length, r - l)
                cur_sum -= nums[l]
                l += 1
                
        return min_length if min_length != inf else 0
    
