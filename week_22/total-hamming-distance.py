# https://leetcode.com/problems/total-hamming-distance/

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        mask = 1
        
        for i in range(32):
            ones = 0
            for num in nums:
                if num & mask:
                    ones += 1
            zeros = len(nums) - ones
            
            total += ones * zeros
            mask <<= 1
            
        return total
      
