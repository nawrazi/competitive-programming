# https://leetcode.com/problems/maximum-erasure-value/description/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        window = defaultdict(int)
        cur_val, max_val = 0, 0
        
        while right < len(nums):
            window[nums[right]] += 1
            cur_val += nums[right]
            right += 1
            
            while len(window) < right - left:
                window[nums[left]] -= 1
                cur_val -= nums[left]
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
                
            max_val = max(max_val, cur_val)
            
        return max_val
    
