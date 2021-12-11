# https://github.com/nawrazi/Competitive-Programming/blob/main/week_1/k-closest-points.py

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append([distance,point])

        distances.sort()

        return [distances[i][-1] for i in range(k)]
