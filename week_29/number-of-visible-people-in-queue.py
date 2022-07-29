# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        vis = [0 for _ in range(len(heights))]
        stack = []
        
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            while stack and height > stack[-1]:
                stack.pop()
                vis[i] += 1
            if stack:
                vis[i] += 1
            stack.append(height)
            
        return vis
    
