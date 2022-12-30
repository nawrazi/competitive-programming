# https://leetcode.com/problems/single-threaded-cpu/description/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((task[0], task[1], idx) for idx, task in enumerate(tasks))
        heap = [(tasks[0][1], tasks[0][2], tasks[0][0])]
        task = 1
        time = tasks[0][0]
        order = []
        
        while heap:
            duration, idx, _ = heappop(heap)
            time += duration
            order.append(idx)
            
            while task < len(tasks) and tasks[task][0] <= time:
                heappush(heap, (tasks[task][1], tasks[task][2], tasks[task][0]))
                task += 1
                
            if task < len(tasks) and not heap:
                heappush(heap, (tasks[task][1], tasks[task][2], tasks[task][0]))
                time = tasks[task][0]
                task += 1
                
        return order
    
