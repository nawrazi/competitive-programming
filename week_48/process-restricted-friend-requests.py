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

            for node1, node2 in restrictions:
                if find(node1) == find(node2):
                    parents = backup
                    return False

            return True

        result = []
        for node1, node2 in requests:
            result.append(union(node1, node2))

        return result
    
