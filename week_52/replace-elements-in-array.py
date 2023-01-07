# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {num: idx for idx, num in enumerate(nums)}
        
        for num, rep in operations:
            idx = pos[num]
            nums[idx] = rep
            del pos[num]
            pos[rep] = idx
            
        return nums
    
