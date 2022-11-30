# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        nums.append(0)
        counts = Counter(nums[:k])
        left, right = 0, k
        cur_sum, max_sum = sum(nums[:k]), 0
        
        while right < len(nums):
            if len(counts) == k:
                max_sum = max(cur_sum, max_sum)
                
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            counts[nums[right]] += 1
            
            cur_sum -= nums[left]
            cur_sum += nums[right]
            
            left += 1
            right += 1
            
        return max_sum
    
