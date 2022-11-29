# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = inf
        steps = 0
        
        for num in reversed(nums):
            if num <= prev:
                prev = num
                continue
                
            div = num // prev
            steps += div - 1
            if num % prev != 0:
                prev = num // (div + 1)
                steps += 1
                
        return steps
    
