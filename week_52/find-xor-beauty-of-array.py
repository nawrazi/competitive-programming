# https://leetcode.com/problems/find-xor-beauty-of-array/description/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)
    
