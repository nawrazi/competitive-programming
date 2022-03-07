# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if len(self.heap1) == 0 or len(self.heap2) == 0:
            heapq.heappush(self.heap2, num)

        elif num <= -self.heap1[0]:
            heapq.heappush(self.heap1, -num)

        else:
            heapq.heappush(self.heap2, num)

        while len(self.heap1) > len(self.heap2) + 1:
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))

        while len(self.heap2) > len(self.heap1) + 1:
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

    def findMedian(self) -> float:
        if len(self.heap1) > len(self.heap2):
            return -self.heap1[0]
        elif len(self.heap2) > len(self.heap1):
            return self.heap2[0]
        else:
            return (-self.heap1[0] + self.heap2[0]) / 2
