# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            if bricks < 0:
                return i - 1

            if heights[i] >= heights[i+1]:
                continue

            climb = heights[i+1] - heights[i]
            if ladders == 0:
                bricks -= climb

            elif len(heap) < ladders:
                heapq.heappush(heap, climb)

            elif climb > heap[0]:
                bricks -= heapq.heappop(heap)
                heapq.heappush(heap, climb)

            elif climb <= heap[0]:
                bricks -= climb
                
        return i if bricks < 0 else i + 1
