# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)
        q = deque([('0000', 0)])
        seen = {'0000'}
        
        while q:
            lock, steps = q.popleft()
            
            if lock == target:
                return steps
            if lock in ends:
                continue
            
            for i in range(4):
                for d in [-1, 1]:
                    mid = (int(lock[i]) + d) % 10
                    nex = lock[:i] + str(mid) + lock[i+1:]
                    if nex not in seen:
                        q.append((nex, steps + 1))
                        seen.add(nex)
                        
        return -1
    
