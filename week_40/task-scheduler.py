# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mx = max(count.values())
        rows, cols = mx - 1, n + 1
        schedule = rows * cols
        
        last = 0
        for c in count.values():
            if c == mx:
                last += 1
                
        return max(schedule + last, len(tasks))
    
