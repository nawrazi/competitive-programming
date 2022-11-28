# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        total = numsDivide[0]
        for num in numsDivide:
            total = gcd(total, num)
            
        for ops, num in enumerate(sorted(nums)):
            if total % num == 0:
                return ops
        else:
            return -1
        
