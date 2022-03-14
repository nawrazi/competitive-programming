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
            if len(heap) < ladders:
                heappush(heap, climb)

            elif ladders == 0 or climb <= heap[0]:
                bricks -= climb

            elif climb > heap[0]:
                bricks -= heappop(heap)
                heappush(heap, climb)

        return i if bricks < 0 else i + 1
