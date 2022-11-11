# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        c = len(nums) - 1
        a, b = c - 2, c - 1
        while a >= 0 and nums[a] + nums[b] <= nums[c]:
            a -= 1
            b -= 1
            c -= 1
            
        return nums[a] + nums[b] + nums[c] if a >= 0 else 0
    
