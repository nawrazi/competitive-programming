# https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0 for _ in range(1001)]
        for num, start, end in trips:
            stops[start] += num
            stops[end] -= num
            
        for i in range(1, 1001):
            stops[i] += stops[i - 1]
            
        for stop in stops[:-1]:
            if stop > capacity:
                return False
            
        return True
    
