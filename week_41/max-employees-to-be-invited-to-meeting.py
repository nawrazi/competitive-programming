# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        graph = {}
        parent = defaultdict(list)
        indeg = [0 for _ in favorite]
        seen = set()
        for idx, fav in enumerate(favorite):
            graph[idx] = fav
            parent[fav].append(idx)
            indeg[fav] += 1
            
        def getComponent(start):
            q = deque([start])
            comp = set()
            while q:
                cur = q.popleft()
                comp.add(cur)
                
                if graph[cur] not in seen:
                    q.append(graph[cur])
                    seen.add(graph[cur])
                    
                for nex in parent[cur]:
                    if nex not in seen:
                        q.append(nex)
                        seen.add(nex)
                    
            return comp
        
        def getCycle(comp):
            q = deque()
            for c in comp:
                if indeg[c] == 0:
                    q.append(c)
                    
            top = set()
            while q:
                cur = q.popleft()
                top.add(cur)
                
                nex = graph[cur]
                indeg[nex] -= 1
                if indeg[nex] == 0:
                    q.append(nex)
                    
            return comp - top
        
        def getChain(emp, bad):
            if emp not in parent:
                return 0
            
            chain = 0
            for par in parent[emp]:
                if par != bad:
                    chain = max(chain, 1 + getChain(par, bad))
                    
            return chain
        
        circles, pairs = 0, 0
        for idx, fav in enumerate(favorite):
            if idx not in seen:
                cycle = getCycle(getComponent(idx))
                if len(cycle) == 2:
                    emp1, emp2 = cycle.pop(), cycle.pop()
                    pairs += 2 + getChain(emp1, emp2) + getChain(emp2, emp1)
                else:
                    circles = max(circles, len(cycle))
                    
        return max(circles, pairs)
    
