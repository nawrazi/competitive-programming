# https://leetcode.com/problems/evaluate-division/description/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
            
        def getValue(start, target):
            q = deque([(start, [])])
            seen = {start}
            
            while q:
                var, path = q.popleft()
                
                if var in graph and var == target:
                    res = 1
                    for num in path:
                        res *= num
                    return res
                
                for ngh, val in graph[var]:
                    if ngh not in seen:
                        q.append((ngh, path + [val]))
                        seen.add(ngh)
                        
            return -1
        
        for query in queries:
            yield getValue(*query)
        
