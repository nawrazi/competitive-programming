# https://leetcode.com/problems/build-a-matrix-with-conditions/description/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph = [[[], []] for _ in range(k + 1)]
        indeg = [[0, 0] for _ in range(k + 1)]
        order = [[], []]
        
        for above, below in rowConditions:
            graph[above][0].append(below)
            indeg[below][0] += 1
            
        for left, right in colConditions:
            graph[left][1].append(right)
            indeg[right][1] += 1
            
        def sort(rc):
            queue = deque()
            for num in range(1, k + 1):
                if indeg[num][rc] == 0:
                    queue.append((num, k - 1))
                    
            while queue:
                num, level = queue.popleft()
                order[rc].append(num)
                
                for nex in graph[num][rc]:
                    indeg[nex][rc] -= 1
                    if indeg[nex][rc] == 0:
                        queue.append((nex, level + 1))
                        
            return len(order[rc]) == k
        
        if not sort(0) or not sort(1):
            return []
        
        matrix = [[0] * k for _ in range(k)]
        final = defaultdict(lambda: [0, 0])
        
        for place in range(k):
            final[order[0][place]][0] = place
            final[order[1][place]][1] = place
            
        for num in range(1, k + 1):
            matrix[final[num][0]][final[num][1]] = num
            
        return matrix
    
