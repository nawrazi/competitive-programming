# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        d = {}
        mono_stack = []
        
        for _ in range(2):
            for i, num in enumerate(nums):
                while mono_stack and num > mono_stack[-1][0]:
                    d[mono_stack.pop()[1]] = num
                    
                mono_stack.append((num, i))
                
        return [d.get(i, -1) for i in range(len(nums))]
    
