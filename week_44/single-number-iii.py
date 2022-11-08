# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for num in nums:
            total ^= num
            
        for i, bit in enumerate(reversed(bin(total))):
            if bit == '1':
                first_on = 1 << i
                break
                
        on_group, off_group = 0, 0
        for num in nums:
            if num & first_on:
                on_group ^= num
            else:
                off_group ^= num
                
        return [on_group, off_group]
    
