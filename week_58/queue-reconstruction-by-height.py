# https://leetcode.com/problems/queue-reconstruction-by-height/description/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        
        for k, h in sorted([k, -h] for h, k in people):
            idx = 0
            front = k
            while idx < len(queue) and front > 0:
                if queue[idx][0] >= -h:
                    front -= 1
                idx += 1
            queue.insert(idx, [-h, k])
            
        return queue
    
