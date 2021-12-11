class Solution(object):
    def kClosest(self, points, k):
        for i in range(len(points)):
                distance_squared = (points[i][1])**2 + (points[i][0])**2
                points[i] = [distance_squared, points[i]]

        points.sort(key = lambda point: point[0])

        return [points[i][1] for i in range(k)]
