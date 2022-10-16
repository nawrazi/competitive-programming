# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        graph = {}
        parent = [[] for _ in favorite]
        indeg = [0 for _ in favorite]
        seen = set()
        for idx, fav in enumerate(favorite):
            graph[idx] = fav
            parent[fav].append(idx)
            indeg[fav] += 1
            
        def getComponent(start):
            q = deque([start])
            component = set()
            while q:
                cur = q.popleft()
                component.add(cur)
                
                for nex in parent[cur] + [graph[cur]]:
                    if nex not in seen:
                        q.append(nex)
                        seen.add(nex)
                        
            return component
        
        def getCycle(component):
            q = deque(filter(lambda c: indeg[c] == 0, component))
            topsort = set()
            while q:
                cur = q.popleft()
                topsort.add(cur)
                
                indeg[graph[cur]] -= 1
                if indeg[graph[cur]] == 0:
                    q.append(graph[cur])
                    
            return component - topsort
        
        def getChain(emp, bad):
            chain = 0
            for par in parent[emp]:
                if par != bad:
                    chain = max(chain, 1 + getChain(par, bad))
                    
            return chain
        
        circles, pairs = 0, 0
        for idx in range(len(favorite)):
            if idx not in seen:
                cycle = getCycle(getComponent(idx))
                if len(cycle) == 2:
                    emp1, emp2 = cycle.pop(), cycle.pop()
                    pairs += 2 + getChain(emp1, emp2) + getChain(emp2, emp1)
                else:
                    circles = max(circles, len(cycle))
                    
        return max(circles, pairs)
    
