# https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = {0}
        
        while queue:
            room = queue.popleft()
            
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
                    
        return len(visited) == len(rooms)
    
