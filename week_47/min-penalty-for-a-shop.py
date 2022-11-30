# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        closed = [0]
        opened = [0]
        for log in customers:
            if log == 'Y':
                closed.append(1 + closed[-1])
                opened.append(opened[-1])
            else:
                closed.append(closed[-1])
                opened.append(1 + opened[-1])
        
        min_penalty = inf
        best_time = 0
        for time in range(len(closed)):
            penalty = opened[time] + closed[-1] - closed[time]
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = time
                
        return best_time
    
