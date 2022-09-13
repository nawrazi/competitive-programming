# https://leetcode.com/problems/frog-position-after-t-seconds/

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
            
        children = {n: len(c) for n, c in graph.items()}
        q = deque([(1, 1, 0)])
        seen = {1}
        final = 1
        while q:
            node, prob, time = q.popleft()
            c = children.get(node, 0)
            
            if node == target:
                if time == t or (time < t and c == 0):
                    return prob
                else:
                    return 0
                
            if c == 0:
                final = prob
                continue
                
            for nex in graph[node]:
                if nex not in seen:
                    q.append((nex, prob / c, time + 1))
                    seen.add(nex)
                    children[nex] -= 1
                    
        return final
    
