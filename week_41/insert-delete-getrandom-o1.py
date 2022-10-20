# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.start = 1
        self.vals = [inf]
        self.indexes = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            self.vals.append(val)
            self.indexes[val] = len(self.vals) - 1
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.indexes:
            idx = self.indexes[val]
            self.vals[idx] = self.vals[self.start]
            self.vals[self.start] = inf
            del self.indexes[val]
            self.start += 1
            self.indexes[self.vals[idx]] = idx
            return True
        
    def getRandom(self) -> int:
        idx = random.randint(self.start, len(self.vals) - 1)
        return self.vals[idx]
    
