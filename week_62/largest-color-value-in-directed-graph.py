# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = [[] for _ in colors]
        indeg = [0 for _ in colors]
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
            
        @cache
        def getCounts(node):
            nonlocal pro
            pro += 1
            cur = {}
            for nex in graph[node]:
                if nex in seen:
                    self.cycle = True
                    break
                seen.add(nex)
                counts = getCounts(nex)
                seen.remove(nex)
                for k, v in counts.items():
                    cur[k] = max(cur.get(k, 0), v)
                    
            cur[colors[node]] = cur.get(colors[node], 0) + 1
            return cur
        
        self.cycle = False
        largest = 0
        pro = 0
        for node in range(len(colors)):
            if indeg[node] == 0:
                seen = {node}
                counts = getCounts(node)
                largest = max(largest, max(counts.values()))
                if self.cycle:
                    return -1
                
        return largest if pro == len(colors) else -1
    
