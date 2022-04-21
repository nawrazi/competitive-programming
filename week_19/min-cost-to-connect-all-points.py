# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [-1 for i in range(len(points))]

        def find(point):
            if parents[point] < 0:
                return point, abs(parents[point])
            parent, rank = find(parents[point])
            parents[point] = parent
            return parent, rank

        def union(point1, point2):
            parent1, rank1 = find(point1)
            parent2, rank2 = find(point2)
            if rank2 > rank1:
                rank1, rank2 = rank2, rank1
                parent1, parent2 = parent2, parent1
            if parent1 != parent2:
                parents[parent2] = parent1
                parents[parent1] = -(rank1 + rank2)
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

        min_cost = 0
        connected = 0
        while heap and connected < len(points):
            dist, point1, point2 = heappop(heap)
            if union(point1, point2):
                min_cost += dist
                connected += 1

        return min_cost
