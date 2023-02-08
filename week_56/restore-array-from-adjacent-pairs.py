# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
            
        q = deque()
        for num in indeg:
            if indeg[num] == 1:
                q.append(num)
                break
                
        order = []
        while q:
            num = q.popleft()
            indeg[num] = inf
            order.append(num)
            for ngh in graph[num]:
                indeg[ngh] -= 1
                if indeg[ngh] <= 1:
                    q.append(ngh)
                    
        return order
    
