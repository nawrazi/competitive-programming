# https://leetcode.com/problems/process-restricted-friend-requests/description/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parents = [-1 for _ in range(n)]

        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            nonlocal parents
            parent1, parent2 = find(node1), find(node2)
            backup = parents[:]
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1

            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1

            for u, v in restrictions:
                if find(u) == find(v):
                    parents = backup
                    return False

            return True

        return [union(u, v) for u, v in requests]
    
