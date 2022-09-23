# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            cur = [num, num]
            while stack and cur[0] > stack[-1][0]:
                cur[1] = min(cur[1], stack.pop()[1])
                
            if stack and stack[-1][1] < cur[0] < stack[-1][0]:
                return True
            
            stack.append(cur)
            
        return False
    
