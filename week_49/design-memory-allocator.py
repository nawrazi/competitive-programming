# https://leetcode.com/problems/design-memory-allocator/description/

class Allocator:

    def __init__(self, n: int):
        self.memory = [0 for _ in range(n)]
        self.alloc = defaultdict(list)
        self.size = n
        
    def allocate(self, size: int, mID: int) -> int:
        if size > self.size:
            return -1
        
        for i in range(len(self.memory) - size + 1):
            if self.memory[i] == 0:
                for j in range(i, i + size):
                    if self.memory[j] != 0:
                        break
                else:
                    for j in range(i, i + size):
                        self.memory[j] = mID
                    self.alloc[mID].append((i, size))
                    self.size -= size
                    return i
        
        return -1
    
    def free(self, mID: int) -> int:
        freed = 0
        for idx, size in self.alloc[mID]:
            freed += size
            for i in range(idx, idx + size):
                self.memory[i] = 0
                
        self.size += freed
        del self.alloc[mID]
        return freed
    
