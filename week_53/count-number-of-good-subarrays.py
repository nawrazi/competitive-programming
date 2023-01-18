# https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        total = 0
        window = Counter()
        left, right = 0, 0
        good = 0
        
        while right < len(nums):
            total += window[nums[right]]
            window[nums[right]] += 1
            
            while total >= k:
                good += len(nums) - right
                window[nums[left]] -= 1
                total -= window[nums[left]]
                left += 1
                
            right += 1
            
        return good
    
