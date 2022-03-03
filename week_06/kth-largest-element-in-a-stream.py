# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)

        self.heap = nums

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]

        elif val>self.heap[0] and len(self.heap)==self.k:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
            return self.heap[0]

        else:
            return self.heap[0]
