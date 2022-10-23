# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.indexes = defaultdict(set)
        
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.indexes[val].add(len(self.vals) - 1)
        return len(self.indexes[val]) == 1
    
    def remove(self, val: int) -> bool:
        if len(self.indexes[val]) == 0:
            return False
        
        index = self.indexes[val].pop()
        last = len(self.vals) - 1
        self.vals[index], self.vals[last] = self.vals[last], self.vals[index]
        self.indexes[self.vals[index]].add(index)
        self.indexes[self.vals[index]].remove(last)
        self.vals.pop()
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.vals)
    
