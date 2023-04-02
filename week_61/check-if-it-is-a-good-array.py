# https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
    
