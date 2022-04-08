# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        @lru_cache(None)
        def is_safe(idx):
            if idx in path:
                return False

            path.add(idx)
            safe = True
            for neighbor in graph[idx]:
                safe = safe and is_safe(neighbor)

            return safe

        path = set()
        safes = []

        for i in range(len(graph)):
            path.clear()
            if is_safe(i):
                safes.append(i)

        return safes
