# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)] # id, val
        self.cur_snap = 0
        
    def set(self, index: int, val: int) -> None:
        if self.array[index][-1][0] == self.cur_snap:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.cur_snap, val])
            
    def snap(self) -> int:
        self.cur_snap += 1
        return self.cur_snap - 1
    
    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        start, end = 0, len(history) - 1
        last = 0
        
        while start <= end:
            mid = (start + end) // 2
            if history[mid][0] <= snap_id:
                last = history[mid][1]
                start = mid + 1
            else:
                end = mid - 1
                
        return last
    
