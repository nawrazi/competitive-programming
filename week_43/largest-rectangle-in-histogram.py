# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution: 
    def largestRectangleArea(self, heights: List[int]) -> int:
        bounds = [[-1, len(heights)] for _ in heights]
        
        stack = []
        for i, height in enumerate(heights):
            while stack and height < stack[-1][0]:
                _, idx = stack.pop()
                bounds[idx][1] = i
                
            stack.append((height, i))
            
        stack.clear()
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < stack[-1][0]:
                _, idx = stack.pop()
                bounds[idx][0] = i
                
            stack.append((heights[i], i))
            
        max_area = 0
        for height, (left, right) in zip(heights, bounds):
            width = right - left - 1
            max_area = max(max_area, width * height)
            
        return max_area
    
