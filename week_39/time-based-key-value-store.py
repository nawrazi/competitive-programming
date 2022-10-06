# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        start, end = 0, len(self.map[key]) - 1
        best = -1
        while start <= end:
            mid = (start + end) // 2
            if self.map[key][mid][0] <= timestamp:
                start = mid + 1
                best = mid
            else:
                end = mid - 1
                
        return self.map[key][best][1] if best != -1 else ''
    
