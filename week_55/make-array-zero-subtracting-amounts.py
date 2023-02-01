# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        base = 0
        steps = 0
        
        while nums and nums[-1] == 0:
            nums.pop()
            
        while nums:
            base += nums[-1] - base
            steps += 1
            while nums and nums[-1] - base <= 0:
                nums.pop()
                
        return steps
    
