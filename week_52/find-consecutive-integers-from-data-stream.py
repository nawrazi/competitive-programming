# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.recent = 0
        
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.recent += 1
        else:
            self.recent = 0
            
        return self.recent >= self.k
    
