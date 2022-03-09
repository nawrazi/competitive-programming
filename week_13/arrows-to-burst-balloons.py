# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows = 0

        i = 0
        while i < len(points):
            start, end = points[i]
            while i + 1 < len(points) and end >= points[i+1][0]:
                i += 1
                
            i += 1
            arrows += 1

        return arrows
