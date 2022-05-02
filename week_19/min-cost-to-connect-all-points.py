# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [-1 for i in range(len(points))]
        
        def find(point):
            if parents[point] < 0:
                return point
            parents[point] = find(parents[point])
            return parents[point]
        
        def union(point1, point2):
            parent1, parent2 = find(point1), find(point2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
                return True
        
        def distance(point1, point2):
            x1, y1 = points[point1][0], points[point1][1]
            x2, y2 = points[point2][0], points[point2][1]
            return abs(x1 - x2) + abs(y1 - y2)
        
        heap = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                dist = distance(i, j)
                heappush(heap, (dist, i, j))
                
        total = 0
        connected = 0
        while heap and connected < len(points):
            dist, point1, point2 = heappop(heap)
            if union(point1, point2):
                total += dist
                connected += 1
                
        return total
