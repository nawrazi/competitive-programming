# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append([distance,point])

        distances.sort()

        return [distances[i][-1] for i in range(k)]
