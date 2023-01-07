# https://leetcode.com/problems/race-car/description/

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)])
        seen = {(0, 1)}
        
        while q:
            steps, pos, speed = q.popleft()
            
            if pos == target:
                return steps
            
            acc = pos + speed, speed * 2
            rev = pos, -1 if speed > 0 else 1
            
            if acc not in seen:
                q.append((steps + 1, *acc))
                seen.add(acc)
                
            if rev not in seen and ((speed > 0 and acc[0] > target) or (speed < 0 and acc[0] < target)):
                q.append((steps + 1, *rev))
                seen.add(rev)
                
