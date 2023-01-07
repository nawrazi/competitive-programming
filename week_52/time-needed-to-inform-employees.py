# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = [[] for _ in range(n)]
        
        for node, parent in enumerate(manager):
            if parent != -1:
                tree[parent].append(node)
                
        queue = deque([(headID, 0)])
        max_time = 0
        
        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            
            for child in tree[node]:
                queue.append((child, time + informTime[node]))
                
        return max_time
    
