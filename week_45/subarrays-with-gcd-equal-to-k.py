# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        total = 0
        
        for i, num in enumerate(nums):
            if num == k:
                total += 1
            divisor = num
            for j in range(i + 1, len(nums)):
                divisor = gcd(divisor, nums[j])
                if divisor == k:
                    total += 1
                    
        return total
    
