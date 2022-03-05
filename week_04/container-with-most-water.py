# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, -1
        max_area = 0

        while right>=left:
            area = (right-left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1

        return max_area
