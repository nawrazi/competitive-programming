# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        graph = defaultdict(set)
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
            
        q = deque([(n, 0) for n, e in graph.items() if len(e) == 1])
        
        levels = defaultdict(list)
        while q:
            cur, lev = q.popleft()
            levels[lev].append(cur)
            
            for nex in graph[cur]:
                graph[nex].remove(cur)
                if len(graph[nex]) == 1:
                    q.append((nex, lev + 1))
                    
        return levels[max(levels.keys())]
    
