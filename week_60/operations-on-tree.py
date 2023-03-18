# https://leetcode.com/problems/operations-on-tree/description/

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [-1 for _ in parent]
        self.tree = [[] for _ in parent]
        for node, par in enumerate(parent):
            if par != -1:
                self.tree[par].append(node)
                
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True
    
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True
    
    def upgrade(self, num: int, user: int) -> bool:
        def descendants(node):
            if self.locked[node] != -1:
                return True
            
            found = False
            for child in self.tree[node]:
                if descendants(child):
                    return True
                
        def ancestors(node):
            if self.locked[node] != -1:
                return False
            if node == 0:
                return True
            return ancestors(self.parent[node])
        
        def free(node):
            self.locked[node] = -1
            for child in self.tree[node]:
                free(child)
                
        if self.locked[num] == -1 and descendants(num) and ancestors(num):
            free(num)
            self.locked[num] = user
            return True
        
