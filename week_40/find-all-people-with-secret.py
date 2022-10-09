# https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parents = [-1 for _ in range(n)]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
            
        union(0, firstPerson)
        time = 0
        cur = []
        for p1, p2, t in sorted(meetings, key=lambda x: x[2]):
            if t > time:
                for i in cur:
                    if find(i) != find(0):
                        parents[i] = -1
                time = t
                cur.clear()
                
            union(p1, p2)
            cur.append(p1)
            cur.append(p2)
            
        return [i for i in range(n) if find(i) == find(0)]
    
