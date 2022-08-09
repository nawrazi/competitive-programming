# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.mono_stack = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.mono_stack and price >= self.mono_stack[-1][0]:
            span += self.mono_stack.pop()[1]
            
        self.mono_stack.append((price, span))
        return span
    
