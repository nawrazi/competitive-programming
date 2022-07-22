# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        for row in wall:
            for i in range(len(row)):
                if i != 0:
                    row[i] += row[i-1]
                edges[row[i]] += 1
            
        crosses = [len(wall) - edge for _, edge in sorted(edges.items())]
        crosses.pop()
        
        return min(crosses) if crosses else len(wall)
    
