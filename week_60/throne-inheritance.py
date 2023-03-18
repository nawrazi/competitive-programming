# https://leetcode.com/problems/throne-inheritance/description/

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.children = defaultdict(list)
        self.parent = {}
        self.last = defaultdict(int)
        
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.parent[childName] = parentName
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def successor(self, name, idx):
        if idx >= len(self.children[name]):
            if name == self.king:
                return
            return self.successor(self.parent[name], self.last[self.parent[name]])
        self.last[name] += 1
        return self.children[name][idx]
    
    def getInheritanceOrder(self) -> List[str]:
        order = [self.king]
        nex = self.successor(self.king, 0)
        while nex:
            order.append(nex)
            nex = self.successor(nex, 0)
            
        self.last.clear()
        return [person for person in order if person not in self.dead]
    
