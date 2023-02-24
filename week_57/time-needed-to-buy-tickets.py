# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((count, idx) for idx, count in enumerate(tickets))
        target = tickets[k]
        time = 0
        
        while target > 0:
            count, idx = queue.popleft()
            time += 1
            if count > 1:
                queue.append((count - 1, idx))
            if idx == k:
                target -= 1
                
        return time
    
