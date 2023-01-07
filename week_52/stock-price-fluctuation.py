# https://leetcode.com/problems/stock-price-fluctuation/description/

class StockPrice:

    def __init__(self):
        self.price = {}
        self.max_heap = []
        self.min_heap = []
        self.recent = 0
        
    def update(self, timestamp: int, price: int) -> None:
        self.price[timestamp] = price
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))
        self.recent = max(self.recent, timestamp)
        
    def current(self) -> int:
        return self.price[self.recent]
    
    def maximum(self) -> int:
        while -self.max_heap[0][0] != self.price[self.max_heap[0][1]]:
            heappop(self.max_heap)
            
        return -self.max_heap[0][0]
    
    def minimum(self) -> int:
        while self.min_heap[0][0] != self.price[self.min_heap[0][1]]:
            heappop(self.min_heap)
            
        return self.min_heap[0][0]
    
