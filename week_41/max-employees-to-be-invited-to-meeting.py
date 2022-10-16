# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        fans = [[] for _ in favorite]
        indegrees = [0 for _ in favorite]
        seen = set()
        for fan, fav in enumerate(favorite):
            fans[fav].append(fan)
            indegrees[fav] += 1
            
        def getCycle(start):
            q = deque([start])
            cycle = set()
            while q:
                emp = q.popleft()
                cycle.add(emp)
                
                for ngh in fans[emp] + [favorite[emp]]:
                    if ngh not in seen:
                        q.append(ngh)
                        seen.add(ngh)
                        
            q = deque(filter(lambda c: indegrees[c] == 0, cycle))
            while q:
                emp = q.popleft()
                cycle.remove(emp)
                
                indegrees[favorite[emp]] -= 1
                if indegrees[favorite[emp]] == 0:
                    q.append(favorite[emp])
                    
            return cycle
        
        def getChain(emp, bad):
            chain = 0
            for fan in fans[emp]:
                if fan != bad:
                    chain = max(chain, 1 + getChain(fan, bad))
                    
            return chain
        
        circles, pairs = 0, 0
        for idx in range(len(favorite)):
            if idx not in seen:
                cycle = getCycle(idx)
                if len(cycle) == 2:
                    emp1, emp2 = cycle.pop(), cycle.pop()
                    pairs += 2 + getChain(emp1, emp2) + getChain(emp2, emp1)
                else:
                    circles = max(circles, len(cycle))
                    
        return max(circles, pairs)
    
