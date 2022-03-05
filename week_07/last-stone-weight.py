# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*stone for stone in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            first = heapq.heappop(heap) * -1
            second = heapq.heappop(heap) * -1

            if first!=second:
                heapq.heappush(heap,second-first)

        return abs(heap[0]) if len(heap)==1 else 0
