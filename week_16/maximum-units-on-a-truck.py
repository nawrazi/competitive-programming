# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxes: List[List[int]], truckSize: int) -> int:
        boxes.sort(key = lambda x : x[1], reverse = True)
        units = 0

        for i in range(len(boxes)):
            units += min(boxes[i][0], truckSize) * boxes[i][1]
            truckSize -= min(boxes[i][0], truckSize)

        return units
